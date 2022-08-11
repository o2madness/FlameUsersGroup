import flame

action2 = flame.batch.create_node("Action")
action2.name = "deform"
action2.note = "build after video wall"

action2_media = action2.add_media()
action2_media.name = "collage_texture"


action1 = flame.batch.get_node("collage")

flame.batch.connect_nodes(action1, action1.output_sockets[0], action2_media, "Front")

flame.batch.organize()

# action2.go_to()
a2_difuse_map = action2.create_node("Diffuse Map")

a2_light1 = action2.create_node("Light")
a2_light1.name = "top_left_light"
# a2_light1.position(-710.92, 225.0, 216.57)

a2_light2 = action2.create_node("Light")
a2_light2.name = "bottom_right_light"
# a2_light2.position(-258.94, -192, 267.57)


