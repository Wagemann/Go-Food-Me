from model import Post

from bson.objectid import ObjectId
import motor.motor_asyncio

client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://root:password@mongo')
database = client.PostList
collection = database.post

def move_ids_around(doc):
    document = doc.copy()
    document["id"] = str(document["_id"])
    del document["_id"]
    return document

async def fetch_one_post(id):
    o_id = ObjectId(id)
    document = await collection.find_one({"id": o_id})
    print(document)
    return document

async def fetch_all_post():
    post = []
    cursor = collection.find({})
    async for document in cursor:
        doc = move_ids_around(document)
        post.append(Post(**doc))
    return post

async def create_post(Post):
    document = Post 
    result = await collection.insert_one(document)
    return document

async def update_post(id = None, title = None, description = None, requested_amount = None):
    var = {}
    o_id = ObjectId(id)
    if id:
        var["id"] = o_id
    if title:
        var["title"] = title
    if description:
        var["description"] = description
    if requested_amount:
        var["requested_amount"] = requested_amount    
    await collection.update_one({"id": o_id}, {"$set": var})
    document = await collection.find_one({"id":o_id})
    return document

async def remove_post(id):
    o_id = ObjectId(id)
    await collection.delete_one({"id":o_id})
    return True