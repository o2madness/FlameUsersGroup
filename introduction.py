import flame
# flame.batch.go_to()

# Create action node
action1 = flame.batch.create_node("Action")
action1.name = "myText"
action1.note = "This was created using a script"
action1.note_collapsed = False

comp1 = flame.batch.create_node("Comp")
comp1.name = "Diffuse"
comp1.flame_blend_mode = "Add"

comp2 = flame.batch.create_node("Comp")
comp2.name = "Blur"

flame.batch.connect_nodes(comp1, "Result", comp2, "Front")

flame.batch.connect_nodes(action1, "output1 [ Comp ]", comp1, "Front")

flame.batch.organize()

line01 = action1.create_node("3D Text")
line01.name = "line01"

line01.text = "Name:"