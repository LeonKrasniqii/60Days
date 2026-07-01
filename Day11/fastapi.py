from fastapi import FastAPI , HTTPException
from app.schemas import PostCreate,PostResponse
app= FastAPI()

text_posts = {
    1: {"title":"New Post","content":"cool test post"},
    2: {"title":"Python Tip","content":"cool test posts"},
    3: {"title":"Daily Motivation","content":"cool test post"},
    4: {"title":"Fun Fact","content":"cool test post"},
    5: {"title":"Update","content":"cool test post"},
    6: {"title":"Tech Insight","content":"cool test post"},
    7: {"title":"Quote","content":"cool test post"},
    8: {"title":"Weekend Plans","content":"cool test post"},
    9: {"title":"Question","content":"cool test post"},
    10: {"title":"Mini Announcement","content":"cool test post"}
    }

@app.get("/posts")
def get_all_posts(limit: int ):
    if limit:
        return text_posts[:limit]
    return text_posts

@app.get("/posts/{id}")
def get_post(id: int) -> list[PostResponse]:
    if id not in text_posts:
        raise HTTPException(status_code=404, detail="Post not found")
    
    return text_posts.get(id)

@app.post("/posts")
def create_post(post: PostCreate) -> PostResponse:
    new_post = {"title": post.title, "content":post.content}
    text_posts[max(text_posts.keys()) +1 ] = new_post
    return {}