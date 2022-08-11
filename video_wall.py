import os
from os import listdir
import flame

image_path = "/Users/javiermendezkaram/Pictures/CineSys/UsersGroups2022/"

# Create action node
action1 = flame.batch.create_node("Action")
action1.name = "collage"
action1.note = "This was created using a script"
action1.note_collapsed = False

i=1
j=0
media = []
clip = []
resize = []

# Reading all images in the folder
for image in os.listdir(image_path):
    if ( image.endswith(".png") or image.endswith(".jpg") or image.endswith(".jpeg") ):
        # Creating clips based on the images read: clip1 clip2 clip3
        clip.append("clip" + str(i))
        clip[j] = flame.batch.import_clip( os.path.join(image_path, image) , flame.batch.reels[0].name.get_value() )

        # Creating media layers based on the images read: media1 media2 media 3
        media.append("media" + str(i))
        media[j] = action1.add_media()
        image_name = image.split(".")[0]

        # Creating Resize nodes
        resize.append("resize" + str(i))
        resize[j] = flame.batch.create_node("Resize")
        resize[j].note = "This should have a Crop Edges mode"
        resize[j].note_collapsed = True

        # Connecting the clips to the media layers
        flame.batch.connect_nodes(clip[j], clip[j].output_sockets[0], resize[j], "Front")
        flame.batch.connect_nodes(resize[j], resize[j].output_sockets[0], media[j], "Front")
        
        i += 1
        j += 1

flame.batch.organize()

axis_pivot = action1.create_node("Axis")
axis_pivot.name = "axis_pivot"


# Video wall element details
image_width = 1920.0
image_height = 1080.0
cols = 3

row = 0
col_step = 0

my_axs = []
for axs in range(j):
    my_axs.append("axis"+str(axs+1))
    my_axs[axs] = action1.get_node("axis"+str(axs+1))
    
    if (col_step == cols):
        row += 1
        col_step = 0
    my_axs[axs].position = ( image_width * col_step, + (image_height * row), 0.0)
    col_step +=1
   
for axs in range(j):
    action1.connect_nodes( axis_pivot, my_axs[axs], "Default")

action1.organize()