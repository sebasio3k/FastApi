from fastapi import FastAPI, HTTPException, Query, Body

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

@app.get("/")
def home():
    return {'message': 'Welcome to the Mini Blog! :)'}

@app.get("/posts")
def list_all_posts():
    # return BLOG_POSTS
    return {"data": BLOG_POSTS}

@app.get("/post")
def list_post(query: str | None = Query(default=None, description="Text to search for in the post titles.")):
    if query:
        filtered_posts = [post for post in BLOG_POSTS if query.lower() in post["title"].lower()]
        print(f'Filtered posts: {filtered_posts}')
        return {"data": filtered_posts, "query": query}
    else:
        return {"data": "No search query provided."}
    
@app.get("/post/{post_id}")
def get_post(post_id: int, include_content: bool = Query(default=True, description="Whether to include the content of the post in the response.")):
    data = []
    for post in BLOG_POSTS:
        if post["id"] == post_id:
            if not include_content:
                data = {key: value for key, value in post.items() if key != "content"}
            else:
                data = post
            break
    # post = next((post for post in BLOG_POSTS if post["id"] == post_id), None)
    if data:
        return {"data": data}
    else:
        return {"error": "Post not found."}
    
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

@app.put("/post/{post_id}")
def uptade_post(post_id: int, data: dict = Body(..., description="Info to upload")):
    
    for post in BLOG_POSTS:
        if post['id'] == post_id:
            if "title" in data: post["title"] = data["title"]
            if "content" in data:
                post["content"] = data["content"]
            return {"message": "Post updated", "data": post}
    
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