#!/usr/bin/python
"""
 Author: James A. Shackleford
   Date: Oct. 16th, 2015

   A simple implementation of Conway's Game of Life
"""
import patterns
import sys
import argparse
import random
import numpy
from matplotlib import pyplot as plt
from matplotlib import animation


def generate_world(opts):
    """
    Accepts: opts  -- parsed command line options
    Returns: world -- a list of lists that forms a 2D pixel buffer

    Description: This function generates a 2D pixel buffer with dimensions
                 opts.cols x opts.rows (in pixels).  The initial contents
                 of the generated world is determined by the value provided
                 by opts.world_type: either 'random' or 'empty'  A 'random'
                 world has 10% 'living' pixels and 90% 'dead' pixels.  An
                 'empty' world has 100% 'dead' pixels.
    """
    world = [[0 for x in range(opts.cols)]for x in range(opts.rows)];			# make the world size
    if opts.world_type=='empty':												# make empty world
        return world;    
    if opts.world_type=='random':												# make random world
        for i in range(opts.rows):
			world[i]=numpy.random.choice([0, 1],size=opts.cols,p=[0.9, 0.1]);
        return world;


def update_frame(frame_num, opts, world, img):
    """
    Accepts: frame_num  -- (automatically passed in) current frame number
             opts       -- a populated command line options instance
             world      -- the 2D world pixel buffer
             img        -- the plot image
    """

    # set the current plot image to display the current 2D world matrix
    img.set_array(world)

    # Create a *copy* of 'world' called 'new_world' -- 'new_world' will be
    # our offscreen drawing buffer.  We will draw the next frame to
    # 'new_world' so that we may maintain an in-tact copy of the current
    # 'world' at the same time.
    new_world = []
    for row in range(opts.rows):
        new_world.append(numpy.zeros(opts.cols));
    for rowcount in range(opts.rows):
        for colcount in range(opts.cols):
            if world[rowcount][colcount]==1:
                if count(rowcount,colcount,world,opts)<2:
                    new_world[rowcount][colcount]=0;
                if (count(rowcount,colcount,world,opts)==2)or(count(rowcount,colcount,world,opts)==3):
                    new_world[rowcount][colcount]=1;
                if count(rowcount,colcount,world,opts)>3:
                    new_world[rowcount][colcount]=0;
            else: 
                if count(rowcount,colcount,world,opts)==3:
                    new_world[rowcount][colcount]=1;
            


    # Copy the contents of the new_world into the world
    # (i.e. make the future the present)
    world[:] = new_world[:]
    return img,

def count(rowcount,colcount,world,opts):
    temp=0;
    rowcount2=rowcount+1;
    colcount2=colcount+1;
    if rowcount==opts.rows-1:rowcount2=0;
    if colcount==opts.cols-1:colcount2=0;
    if world[rowcount2][colcount-1]==1:temp=temp+1;
    if world[rowcount2][colcount]==1:temp=temp+1;
    if world[rowcount2][colcount2]==1:temp=temp+1;
    if world[rowcount][colcount-1]==1:temp=temp+1;
    if world[rowcount][colcount2]==1:temp=temp+1;
    if world[rowcount-1][colcount-1]==1:temp=temp+1;
    if world[rowcount-1][colcount]==1:temp=temp+1;
    if world[rowcount-1][colcount2]==1:temp=temp+1;
    return temp;





def blit(world, sprite, x, y):
    """
    Accepts: world  -- a 2D world pixel buffer generated by generate_world()
             sprite -- a 2D matrix containing a pattern of 1s and 0s
             x      -- x world coord where left edge of sprite will be placed
             y      -- y world coord where top edge of sprite will be placed

    Returns: (Nothing)

    Description: Copies a 2D pixel pattern (i.e sprite) into the larger 2D
                 world.  The sprite will be copied into the 2D world with
                 its top left corner being located at world coordinate (x,y)
    """
    for rowcount in range(y,len(sprite)+y):									
        for colcount in range(x,len(sprite[1])+x):
            world[rowcount][colcount]=sprite[rowcount-y][colcount-x];

def run_simulation(opts, world):
    """
    Accepts: opts  -- a populated command line options class instance
             world -- a 2D world pixel buffer generated by generate_world()

    Returns: (Nothing)

    Description: This function generates the plot that we will use as a
                 rendering surfance.  'Living' cells (represented as 1s in
                 the 2D world matrix) will be rendered as black pixels and
                 'dead' cells (represetned as 0s) will be rendered as
                 white pixels.  The method FuncAnimation() accepts 4
                 parameters: the figure, the frame update function, a
                 tuple containing arguments to pass to the update function,
                 and the frame update interval (in milliseconds).  Once the
                 show() method is called to display the plot, the frame
                 update function will be called every 'interval'
                 milliseconds to update the plot image (img).
    """
    if not world:
        print "The 'world' was never created.  Exiting"
        sys.exit()

    fig = plt.figure()
    img = plt.imshow(world, interpolation='none', cmap='Greys', vmax=1, vmin=0)
    ani = animation.FuncAnimation(fig,
                                  update_frame,
                                  fargs=(opts, world, img),
                                  interval=opts.framedelay)

    plt.show()


def report_options(opts):
    """
    Accepts: opts  -- a populated command line options class instance

    Returns: (Nothing)

    Descrption: This function simply prints the parameters used to
                start the 'Game of Life' simulation.
    """

    print "Conway's Game of Life"
    print "====================="
    print "   World Size: %i x %i" % (opts.rows, opts.cols)
    print "   World Type: %s" % (opts.world_type)
    print "  Frame Delay: %i (ms)" % (opts.framedelay)


def get_commandline_options():
    """
    Accepts: (Nothing)

    Returns: opts  -- an instance of the options class that possesses members
                      specified by the 'dest' parameter of the add_option()
                      method.  Members contain the 'default' value unless
                      the user supplies a value from the command line using
                      the appropriate switch (i.e. '-r 100' or '--rows 100')

    optparse module documentation:
    https://docs.python.org/2/library/optparse.html
    """
    parser = argparse.ArgumentParser()

    parser.add_argument('-r', '--rows',
                        help='set # of rows in the world',
                        action='store',
                        type=int,
                        dest='rows',
                        default=100)

    parser.add_argument('-c', '--columns',
                        help='set # of columns in the world',
                        action='store',
                        type=int,
                        dest='cols',
                        default=100)

    parser.add_argument('-w', '--world',
                        help='type of world to generate',
                        action='store',
                        type=str,
                        dest='world_type',
                        default='empty')

    parser.add_argument('-d', '--framedelay',
                        help='time (in milliseconds) between frames',
                        action='store',
                        type=int,
                        dest='framedelay',
                        default=40)

    opts = parser.parse_args()

    return opts


def main():
    """
    The main function -- everything starts here!
    """
    opts = get_commandline_options()
    world = generate_world(opts)
    report_options(opts)

    blit(world, patterns.gosper_gun, 20, 20)    # here is for change the patterns

    run_simulation(opts, world)


if __name__ == '__main__':
    main()
