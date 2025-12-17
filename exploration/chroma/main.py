changes = [
    "Wind Ward has been Removed.",
    "Bullseye now requires Called Shots. Bullseye now applies 10 Critical Weakness (previously 5).",
    "Added a new Mirage Deadeye Ascendancy Passive Skill which grants the Mirage Deadeye Meta Skill. Mirage Deadeye: While active, firing a Ranged Attack Projectile will create a Mirage that uses socketed Ranged Attacks for a short duration, then vanishes. You cannot create another Mirage for a short time after initially creating one.",
]

changes = list(map(lambda change: "[Deadeye] " + change, changes))

import chromadb
from uuid import uuid4

chroma_client = chromadb.HttpClient(host="localhost", port="8005")
collection = chroma_client.create_collection(name=uuid4())
collection.add(ids=[str(i) for i in range(len(changes))], documents=changes)

print(collection.query(query_texts="Deadeye", n_results=1))
