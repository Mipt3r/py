#!/usr/bin/python3
#--------------------------------------
#
#     Minecraft Python API
#        Castle Builder
#
# This script creates a castle complete
# with keep, moat and perimeter walls.
#
# Author : Matt Hawkins
# Date   : 12/02/2021
#
# https://www.raspberrypi-spy.co.uk/
#
#--------------------------------------

# Import Minecraft libraries
import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create()

mc.postToChat("Let's build a castle!")

#--------------------------------------
# Define Functions
#--------------------------------------

def CreateWalls(x,y,z,size,height,material,battlements,walkway):
  # Create 4 walls with a specified size, height and material.
  # Battlements and walkways can also be added to the top edges.
  
  mc.setBlocks(x-size,y+1,z-size,x+size,y+height,z-size,material) 
  mc.setBlocks(x-size,y+1,z-size,x-size,y+height,z+size,material)
  mc.setBlocks(x+size,y+1,z+size,x-size,y+height,z+size,material) 
  mc.setBlocks(x+size,y+1,z+size,x+size,y+height,z-size,material) 

  # Add battlements to top edge
  if battlements==True:
    for q in range(0,(2*size)+1,2):
      mc.setBlock(x-size,y+height+1,z-size+q,material) 
      mc.setBlock(x+size,y+height+1,z-size+q,material) 
      mc.setBlock(x-size+q,y+height+1,z+size,material) 
      mc.setBlock(x-size+q,y+height+1,z-size,material)

  # Add wooden walkways
  if walkway==True:  
    mc.setBlocks(x-size+1,y+height-1,z+size-1,x+size-1,y+height-1,z+size-1,block.WOOD_PLANKS)   
    mc.setBlocks(x-size+1,y+height-1,z-size+1,x+size-1,y+height-1,z-size+1,block.WOOD_PLANKS)  
    mc.setBlocks(x-size+1,y+height-1,z-size+1,x-size+1,y+height-1,z+size-1,block.WOOD_PLANKS)   
    mc.setBlocks(x+size-1,y+height-1,z-size+1,x+size-1,y+height-1,z+size-1,block.WOOD_PLANKS)  

def CreateLandscape(x,y,z,moatwidth,moatdepth,islandwidth):
  # Set upper half to air
  mc.setBlocks(x-moatwidth-2,y,z-moatwidth-2,x+moatwidth+2,y+100,z+moatwidth+2,block.AIR) 
  # Create square of grass
  mc.setBlocks(x-moatwidth-2,y,z-moatwidth-2,x+moatwidth+2,y-1,z+moatwidth+2,block.GRASS)
  # with a block of dirt underneath it
  mc.setBlocks(x-moatwidth-2,y-1,z-moatwidth-2,x+moatwidth+2,y-moatdepth-1,z+moatwidth+2,block.DIRT)  
  # Create water moat
  mc.setBlocks(x-moatwidth,y,z-moatwidth,x+moatwidth,y-moatdepth,z+moatwidth,block.WATER)
  # Create island
  mc.setBlocks(x-islandwidth,y,z-islandwidth,x+islandwidth,y-moatdepth,z+islandwidth,block.GRASS)  

def CreateKeep(x,y,z,size,floors):
  # Create a keep with a specified number
  # of floors floors and a roof
  height=(floors*5)+5
  
  mc.postToChat("  Creating walls ...")
  CreateWalls(x,y,z,size,height,block.STONE_BRICK,True,True)
  
  # Floors & Windows
  mc.postToChat("  Creating floors ...")
  for floor in range(1,floors+1):
    mc.setBlocks(x-size+1,(floor*5)+y,z-size+1,x+size-1,y+(floor*5),z+size-1,block.WOOD_PLANKS)

  # Staircase holes in floors
  mc.postToChat("  Creating stairs ...")
  mc.setBlocks(x-size+1,y+1,z-size+1,x-size+1,y+(floors*5),z-size+3,block.AIR)
  # Stairs
  for floor in range(1,floors+1):
    print("Stairs for floor ",floor)
    mc.setBlock(x-size+1,(floor*5)+y-1,z-size+1,block.WOOD_PLANKS)
    mc.setBlock(x-size+1,(floor*5)+y-2,z-size+2,block.WOOD_PLANKS)
    mc.setBlock(x-size+1,(floor*5)+y-3,z-size+3,block.WOOD_PLANKS)
    mc.setBlock(x-size+1,(floor*5)+y-4,z-size+4,block.WOOD_PLANKS)
    mc.setBlock(x-size+1,(floor*5)+y-2,z-size+5,block.TORCH)

  # Windows
  mc.postToChat("  Creating windows ...")
  for floor in range(1,floors+1):
    CreateWindows(x,(floor*5)+y+2,z+size,"N")
    CreateWindows(x,(floor*5)+y+2,z-size,"S")
    CreateWindows(x-size,(floor*5)+y+2,z,"W")
    CreateWindows(x+size,(floor*5)+y+2,z,"E")

  # Door
  mc.setBlocks(x,y+1,z-size,x,y+2,z-size,block.AIR)

def CreateWindows(x,y,z,dir):

  if dir=="N" or dir=="S":
    z1=z
    z2=z
    x1=x-2
    x2=x+2

  if dir=="E" or dir=="W":
    z1=z-2
    z2=z+2
    x1=x
    x2=x

  mc.setBlocks(x1,y,z1,x1,y+1,z1,block.AIR)
  mc.setBlocks(x2,y,z2,x2,y+1,z2,block.AIR) 

  if dir=="N":
    a=3
  if dir=="S":
    a=2
  if dir=="W":
    a=0
  if dir=="E":
    a=1
  
#--------------------------------------
#
# Configure some variables
#
#--------------------------------------

keepFloors=4
keepSize=5

outerWallHeight=5
innerWallHeight=6

outerWallSize=21
innerWallSize=13

moatDepth=5
moatWidth=5

# Get the position of the player
x, y, z = mc.player.getPos()

#--------------------------------------
#
# Main Script  
#
#--------------------------------------

mc.postToChat("Creating ground and moat ...")
print("Create ground and moat")
CreateLandscape(x,y,z,outerWallSize+2+moatWidth,moatDepth,outerWallSize+2)  

mc.postToChat("Creating outer walls ...")
print("Create outer walls")
CreateWalls(x,y,z,outerWallSize,outerWallHeight,block.STONE_BRICK,True,True)

mc.postToChat("Creating inner walls ...")
print("Create inner walls")
CreateWalls(x,y,z,innerWallSize,innerWallHeight+1,block.STONE_BRICK,True,True)

mc.postToChat("Creating keep ...")
print("Create Keep with 4 levels")
CreateKeep(x,y,z,keepSize,keepFloors)

print("Position player on Keep's top floor")
mc.player.setPos(x,y+(keepFloors*5)+5,z)

mc.postToChat("Finished!")
