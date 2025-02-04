
queue = ["Matti", "Riikka", "Antti", "Jenni", "Anu", "Ville", "Jarno"]

#Matti Leaves the queue
queue.remove("Matti")

#Ville asks Anni to queue on his behalf
queue.remove("Ville")
queue.insert(4, "Anni")

#Jarno leaves the queue
queue.remove("Jarno")

#Marjo Joins the end of the queue
queue.append("Marjo")

#Antti lets two people in front of him
antti_index = queue.index("Antti")
queue.insert(antti_index + 2, queue.pop(antti_index))

# Determine if Jenni is in the queue and her position
is_jenni_in_queue = "Jenni" in queue
jenni_position = queue.index("Jenni") + 1 if is_jenni_in_queue else None

# Determine the third last person in the queue
third_last_person = queue[-3] if len(queue) >= 3 else None

# Print results
print("Final queue:", queue)
print("Is Jenni in the queue?", is_jenni_in_queue)
print("Jenni's position:", jenni_position)
print("Third last person:", third_last_person)