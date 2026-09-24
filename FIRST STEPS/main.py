from fastapi import FastAPI, HTTPException, Query, Body, Path
from pydantic import BaseModel, Field, field_validator, EmailStr
from typing import Optional, List, Union

app = FastAPI(
    title="Mini Blog", 
    description="This is a simple FastAPI application.", 
    version="1.0.0"
)

BLOG_POSTS = [
    {
        "id": 1,
        "title": "First Post",
        "content": "This is the content of the first post."
    },
    {
        "id": 2,
        "title": "Second Post",
        "content": "This is the content of the second post."
    },
    {
        "id": 3,
        "title": "Third Post",
        "content": "This is the content of the third post."
    }
]

BAD_WORDS = ["bad", "word", "test", "example"]

class Tag(BaseModel):
    name: str = Field(
        ..., 
        min_length=2, 
        max_length=30,
        description="The name of the tag.", 
        examples=["This is the name of the tag."]
    )
    
class Author(BaseModel):
    name: str = Field(
        ..., 
        min_length=2, 
        max_length=30,
        description="The name of the author.", 
        examples=["name of the author."]
    )
    email: EmailStr = Field(
        default="",
        description="The email of the author.",
        examples=["email@domain.com"]
    )

class PostBase(BaseModel):
    title: str
    content: str
    tags: Optional[List[Tag]] = Field(default_factory=list) # [] 
    author: Optional[Author] = None
    
class PostCreate(BaseModel):
    title: str = Field(
        ..., 
        min_length=5, 
        max_length=50, 
        description="The title of the post.", 
        examples=["This is the title of the post."]
    ) # ... ellipsis means that the field is required
    content: str = Field(
        default="to be defined...", 
        min_length=10, 
        max_length=100, 
        description="The content of the post.",
        examples=["This is the content of the post."]
    )
    # tags: List[Tag] = []
    tags: List[Tag] = Field(
        default_factory=list,
        examples=[[{"name": "python"}, {"name": "fastapi"}]],
    )
    author: Optional[Author] = None
    
    @field_validator("title")
    @classmethod
    def title_must_be_unique(cls, value: str) -> str:
        if any(post["title"].lower() == value.lower() for post in BLOG_POSTS):
            raise ValueError("Title must be unique.")
        return value
    
    @field_validator("title")
    @classmethod
    def not_allow_bad_words(cls, value):
        for bad_word in BAD_WORDS:
            if bad_word in value:
                raise ValueError("Title cannot contain bad words.")
        return value

# Response Models
class PostPublic(PostBase): 
    id: int
    
class PostSummary(BaseModel):
    id: int
    title: str

class PostUpdate(PostBase):
    pass

class PatchPost(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    tags: Optional[List[Tag]] = None
    

@app.get("/")
def home():
    return {'message': 'Welcome to the Mini Blog! :)'}

@app.get("/posts", response_model=List[PostPublic])
def list_all_posts():
    # return BLOG_POSTS
    return  BLOG_POSTS


@app.get("/post", response_model=List[PostPublic])
def list_post(query: Optional[str] = Query(
        default=None, 
        description="Text to search for in the post titles.",
        alias="search",
        min_length=3,
        max_length=50,
        pattern=r"^[\w\sáéíóúÁÉÍÓüÜ-]+$"
        # pattern=r"^[a-zA-Z]+$"
    )):
    if query:
        filtered_posts = [post for post in BLOG_POSTS if query.lower() in post["title"].lower()]
        print(f'Filtered posts: {filtered_posts}')
        return filtered_posts
    else:
        # return {"data": "No search query provided."}
        return BLOG_POSTS
    

@app.get("/post/{post_id}", response_model=Union[PostSummary,PostPublic], response_description="The post details.")
def get_post(post_id: int = Path(
        ..., 
        gt=0,
        title="Post ID",
        description="The ID of the post to retrieve.",
        examples=[1,2,3]
    ), include_content: bool = Query(default=True, description="Whether to include the content of the post in the response.")):
    for post in BLOG_POSTS:
        print(post)
        if post["id"] == post_id:
            print('entra')
            if not include_content:
                print(f'not include content')
                return {key: value for key, value in post.items() if key != "content"}
            return post

    # post = next((post for post in BLOG_POSTS if post["id"] == post_id), None)
    raise HTTPException(status_code=404, detail="Post not found")
    
@app.post("/newPost")
def create_post(post: dict = Body(..., description="The post data to create.")):
    if "title" not in post or "content" not in post:
        return {"error": "Title and Content are required."}
    
    if not str(post["title"]).strip:
        return {"error": "Title cannot be empty."}
    
    new_id = (BLOG_POSTS[-1]["id"]+1) if BLOG_POSTS else 1
    new_post = {"id": new_id, "title": post["title"], "content": post["content"]}
    BLOG_POSTS.append(new_post)
    
    return {"message": "Post Created", "data": new_post}

@app.post("/newPostv2", response_model=PostPublic, response_description="The created post details.")
def create_post_v2(post: PostCreate):
    new_id = (BLOG_POSTS[-1]["id"]+1) if BLOG_POSTS else 1
    new_post = {
        "id": new_id, 
        "title": post.title, 
        "content": post.content, 
        "tags": [tag.model_dump() for tag in post.tags],
        "author": post.author.model_dump() if post.author else None
    }
    BLOG_POSTS.append(new_post)
    
    # return {"message": "Post Created v2", "data": new_post}
    return new_post

@app.put("/post/{post_id}", response_model=PostPublic, response_description="The updated post details.", response_model_exclude_none=True)
def uptade_post(post_id: int, data: PostUpdate):
    
    for post in BLOG_POSTS:
        if post['id'] == post_id:
            playload = data.model_dump(exclude_unset=True) # model_dump() returns a dictionary
            if "title" in playload: post["title"] = playload["title"]
            if "content" in playload:
                post["content"] = playload["content"]
            # return {"message": "Post updated", "data": post}
            return post
    
    # return {"error": "Post not found"}
    raise HTTPException(status_code=404, detail="Post not found")

@app.patch("/post/{post_id}")
def patch_post(post_id: int, data: PatchPost):
    
    for post in BLOG_POSTS:
        if post['id'] == post_id:
            playload = data.model_dump(exclude_unset=True)
            if "title" in playload: post["title"] = playload["title"]
            if "content" in playload:
                post["content"] = playload["content"]
            # return {"message": "Post updated", "data": post}
            return post
    
    # return {"error": "Post not found"}
    raise HTTPException(status_code=404, detail="Post not found")
    
@app.delete("/post/{post_id}", status_code=204)
def delete_post(post_id: int):
    for index, post in enumerate(BLOG_POSTS):
    # for post in BLOG_POSTS:
        if post["id"] == post_id:
            # BLOG_POSTS.remove(post)
            BLOG_POSTS.pop(index)
            # return {"message": "Post deleted", "data": post}
            return
    
    raise HTTPException(status_code=404, detail="Post not found")