```
                    @         @                 @@@@@       @         @@@@@@@@@@
                  @@@       @@@             @@@@@@@@@@@@@   @@@       @@@@@@@@@@
               @@@@@@    @@@@@@           @@@@@@@@@@@@@@@@@ @@@@@@    @@@@@@@@@@
             @@@@@@@@  @@@@@@@@          @@@@@@@@@@@@@@@@@@@@@@@@@@@  @@@@@@@@@@
          @@@@@@@@@@@@@@@@@@@@@   @@@   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@@@@X@@@@@@@@@ @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
     @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ @@@@@@@@@@@@@@@@@ @@@@@@@@@@@@@@@@@@@@
   @@@@@@@@@@@@@@@@@@@@@@@@@@@X@@@@@@@@@    @@@@@@@@@@@@@   @@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@    @@@           @@@@@       @@@@@@@@@@@@@@@@@@@@

                  @@@@@@      @@@@@@@@@@@@@@@@@@@@          @@@@@@@@@@@@@@@@@@@@
              @@@@@@@@@@@@@   @@@@@@@@@@@@@@@@@@@@          @@@@@@@@@@@@@@@@@@@@
            @@@@@@@@@@@@@@@@@ @@@@@@@@@@@@@@@@@@@@    @@@   @@@@@@@@@@@@@@@@@@@@
           @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ @@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@         @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@     @@@@@@@@@@     
 @@@@@@@@@@@@@@@@@@@          @@@@@@@@@@@@@@@@@@@@ @@@@@@@@@     @@@@@@@@@@     
   @@@@@@@@@@@@@@@            @@@@@@@@@@@@@@@@@@@@    @@@        @@@@@@@@@@     
      @@@@@@@@                @@@@@@@@@@@@@@@@@@@@               @@@@@@@@@@     
```
![Flying Toasters! Prototype by Jack Eastman](/src/tomoya-ikeda-after-dark-flying-toasters-prototype.png)

# Flying Toasters!, Berkeley Systems, 1989
A tribute to the original 1-bit Macintosh After Dark 2.0 screensaver prototype by Jack Eastman and artwork by Tomoya Ikeda.

—

While working on his Ph.D. in the mid ‘80s, Jack Eastman became interested in the possibilities of personal computing with the then new Macintosh. He wanted a screen saver where you could change the channel, so he could show all the different kinds of algorithmic drawings he was doing. Unfortunately in those days there was no concept of a screen saver in the operating system.

A friend of Jack’s from the Lawrence Berkeley Laboratory, Patrick Beard, had gone to work for Berkeley Systems, a small start-up that was doing operating system utilities. Patrick connected Jack with the founder, Wes Boyd, who saw potential in what Jack was doing. They brought the company’s resources to bear on professionalizing what Jack had begun.

Tomoya Ikeda (池田友也) played a key part in the evolution of the famous After Dark Flying Toasters! screensaver. The original prototype artwork was done by Jack Eastman. Ikeda was brought in as a contractor to draw the final 1-bit artwork. Later versions of the toasters were drawn in color by Igor Gasowski and eventually rendered and animated in 3D by Jarir Maani.

—

To run the animation with Pygame:

```
# Create a 320x240 window
display = create_pygame_display(320, 240)
# Run animation for 30 seconds
run_animation(display, duration_ms=30000)
```

The main advantages of using Pygame

- Efficient drawing operations
- Works on any computer with Python
- Provides a window system with proper event handling
- Easier testing and development before deploying to hardware

—

After Dark 2.0 Flying Toasters! © 1990 Berkeley Systems Inc. by Jack Eastman, Bruce Burkhalter, and Patrick Beard. Artwork by Tomoya Ikeda.
