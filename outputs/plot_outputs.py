import re
import matplotlib.pyplot as plt

data = '''
2024-05-16 21:44:56 a4eae8bf3f6b __main__[9078] INFO Loading Dama...
2024-05-16 21:44:56 a4eae8bf3f6b __main__[9078] INFO Loading NNetWrapper...
2024-05-16 21:44:57 a4eae8bf3f6b __main__[9078] WARNING Not loading a checkpoint!
2024-05-16 21:44:57 a4eae8bf3f6b __main__[9078] INFO Loading the Coach...
2024-05-16 21:44:57 a4eae8bf3f6b __main__[9078] INFO Starting the learning process 🎉
2024-05-16 21:44:57 a4eae8bf3f6b Coach[9078] INFO Starting Iter #1 ...
Self Play: 100% 100/100 [11:38<00:00,  6.98s/it]
Checkpoint Directory exists! 
EPOCH ::: 1
Training Net: 100% 29/29 [00:01<00:00, 23.98it/s, Loss_pi=3.88e+00, Loss_v=1.04e+00]
EPOCH ::: 2
Training Net: 100% 29/29 [00:00<00:00, 137.05it/s, Loss_pi=2.73e+00, Loss_v=8.76e-01]
EPOCH ::: 3
Training Net: 100% 29/29 [00:00<00:00, 134.08it/s, Loss_pi=2.32e+00, Loss_v=7.61e-01]
EPOCH ::: 4
Training Net: 100% 29/29 [00:00<00:00, 133.52it/s, Loss_pi=2.16e+00, Loss_v=6.76e-01]
EPOCH ::: 5
Training Net: 100% 29/29 [00:00<00:00, 128.65it/s, Loss_pi=1.98e+00, Loss_v=6.18e-01]
EPOCH ::: 6
Training Net: 100% 29/29 [00:00<00:00, 134.17it/s, Loss_pi=1.88e+00, Loss_v=6.01e-01]
EPOCH ::: 7
Training Net: 100% 29/29 [00:00<00:00, 138.60it/s, Loss_pi=1.77e+00, Loss_v=5.51e-01]
EPOCH ::: 8
Training Net: 100% 29/29 [00:00<00:00, 138.23it/s, Loss_pi=1.69e+00, Loss_v=5.37e-01]
EPOCH ::: 9
Training Net: 100% 29/29 [00:00<00:00, 122.01it/s, Loss_pi=1.62e+00, Loss_v=5.00e-01]
EPOCH ::: 10
Training Net: 100% 29/29 [00:00<00:00, 134.77it/s, Loss_pi=1.58e+00, Loss_v=4.80e-01]
2024-05-16 21:56:40 a4eae8bf3f6b Coach[9078] INFO PITTING AGAINST PREVIOUS VERSION
Arena.playGames (1): 100% 20/20 [02:35<00:00,  7.77s/it]
Arena.playGames (2): 100% 20/20 [03:03<00:00,  9.17s/it]
2024-05-16 22:02:19 a4eae8bf3f6b Coach[9078] INFO NEW/PREV WINS : 30 / 5 ; DRAWS : 5
2024-05-16 22:02:19 a4eae8bf3f6b Coach[9078] INFO ACCEPTING NEW MODEL
Checkpoint Directory exists! 
Checkpoint Directory exists! 
2024-05-16 22:02:19 a4eae8bf3f6b Coach[9078] INFO Starting Iter #2 ...
Self Play: 100% 100/100 [15:04<00:00,  9.04s/it]
Checkpoint Directory exists! 
EPOCH ::: 1
Training Net: 100% 65/65 [00:00<00:00, 119.08it/s, Loss_pi=1.91e+00, Loss_v=5.75e-01]
EPOCH ::: 2
Training Net: 100% 65/65 [00:00<00:00, 126.54it/s, Loss_pi=1.60e+00, Loss_v=5.13e-01]
EPOCH ::: 3
Training Net: 100% 65/65 [00:00<00:00, 124.21it/s, Loss_pi=1.49e+00, Loss_v=4.72e-01]
EPOCH ::: 4
Training Net: 100% 65/65 [00:00<00:00, 127.31it/s, Loss_pi=1.39e+00, Loss_v=4.31e-01]
EPOCH ::: 5
Training Net: 100% 65/65 [00:00<00:00, 123.59it/s, Loss_pi=1.33e+00, Loss_v=4.13e-01]
EPOCH ::: 6
Training Net: 100% 65/65 [00:00<00:00, 124.59it/s, Loss_pi=1.25e+00, Loss_v=3.82e-01]
EPOCH ::: 7
Training Net: 100% 65/65 [00:00<00:00, 125.07it/s, Loss_pi=1.21e+00, Loss_v=3.80e-01]
EPOCH ::: 8
Training Net: 100% 65/65 [00:00<00:00, 127.56it/s, Loss_pi=1.14e+00, Loss_v=3.62e-01]
EPOCH ::: 9
Training Net: 100% 65/65 [00:00<00:00, 124.09it/s, Loss_pi=1.12e+00, Loss_v=3.35e-01]
EPOCH ::: 10
Training Net: 100% 65/65 [00:00<00:00, 127.49it/s, Loss_pi=1.09e+00, Loss_v=3.16e-01]
2024-05-16 22:17:29 a4eae8bf3f6b Coach[9078] INFO PITTING AGAINST PREVIOUS VERSION
Arena.playGames (1): 100% 20/20 [02:56<00:00,  8.81s/it]
Arena.playGames (2): 100% 20/20 [03:01<00:00,  9.09s/it]
2024-05-16 22:23:27 a4eae8bf3f6b Coach[9078] INFO NEW/PREV WINS : 9 / 10 ; DRAWS : 21
2024-05-16 22:23:27 a4eae8bf3f6b Coach[9078] INFO REJECTING NEW MODEL
2024-05-16 22:23:27 a4eae8bf3f6b Coach[9078] INFO Starting Iter #3 ...
Self Play: 100% 100/100 [15:06<00:00,  9.06s/it]
Checkpoint Directory exists! 
EPOCH ::: 1
Training Net: 100% 101/101 [00:00<00:00, 129.92it/s, Loss_pi=1.85e+00, Loss_v=5.94e-01]
EPOCH ::: 2
Training Net: 100% 101/101 [00:00<00:00, 128.57it/s, Loss_pi=1.55e+00, Loss_v=5.06e-01]
EPOCH ::: 3
Training Net: 100% 101/101 [00:00<00:00, 126.95it/s, Loss_pi=1.42e+00, Loss_v=4.81e-01]
EPOCH ::: 4
Training Net: 100% 101/101 [00:00<00:00, 125.89it/s, Loss_pi=1.32e+00, Loss_v=4.59e-01]
EPOCH ::: 5
Training Net: 100% 101/101 [00:00<00:00, 122.93it/s, Loss_pi=1.24e+00, Loss_v=4.30e-01]
EPOCH ::: 6
Training Net: 100% 101/101 [00:00<00:00, 120.67it/s, Loss_pi=1.18e+00, Loss_v=4.19e-01]
EPOCH ::: 7
Training Net: 100% 101/101 [00:00<00:00, 126.98it/s, Loss_pi=1.13e+00, Loss_v=4.02e-01]
EPOCH ::: 8
Training Net: 100% 101/101 [00:00<00:00, 128.62it/s, Loss_pi=1.09e+00, Loss_v=3.72e-01]
EPOCH ::: 9
Training Net: 100% 101/101 [00:00<00:00, 125.59it/s, Loss_pi=1.05e+00, Loss_v=3.61e-01]
EPOCH ::: 10
Training Net: 100% 101/101 [00:00<00:00, 126.97it/s, Loss_pi=1.00e+00, Loss_v=3.37e-01]
2024-05-16 22:38:42 a4eae8bf3f6b Coach[9078] INFO PITTING AGAINST PREVIOUS VERSION
Arena.playGames (1): 100% 20/20 [03:18<00:00,  9.92s/it]
Arena.playGames (2): 100% 20/20 [03:09<00:00,  9.49s/it]
2024-05-16 22:45:10 a4eae8bf3f6b Coach[9078] INFO NEW/PREV WINS : 22 / 0 ; DRAWS : 18
2024-05-16 22:45:10 a4eae8bf3f6b Coach[9078] INFO ACCEPTING NEW MODEL
Checkpoint Directory exists! 
Checkpoint Directory exists! 
2024-05-16 22:45:11 a4eae8bf3f6b Coach[9078] INFO Starting Iter #4 ...
Self Play: 100% 100/100 [14:55<00:00,  8.95s/it]
Checkpoint Directory exists! 
EPOCH ::: 1
Training Net: 100% 137/137 [00:01<00:00, 127.73it/s, Loss_pi=1.07e+00, Loss_v=3.26e-01]
EPOCH ::: 2
Training Net: 100% 137/137 [00:01<00:00, 123.28it/s, Loss_pi=9.90e-01, Loss_v=3.11e-01]
EPOCH ::: 3
Training Net: 100% 137/137 [00:01<00:00, 124.49it/s, Loss_pi=9.54e-01, Loss_v=2.92e-01]
EPOCH ::: 4
Training Net: 100% 137/137 [00:01<00:00, 123.73it/s, Loss_pi=9.18e-01, Loss_v=2.85e-01]
EPOCH ::: 5
Training Net: 100% 137/137 [00:01<00:00, 123.92it/s, Loss_pi=8.88e-01, Loss_v=2.90e-01]
EPOCH ::: 6
Training Net: 100% 137/137 [00:01<00:00, 127.83it/s, Loss_pi=8.59e-01, Loss_v=2.71e-01]
EPOCH ::: 7
Training Net: 100% 137/137 [00:01<00:00, 127.75it/s, Loss_pi=8.53e-01, Loss_v=2.59e-01]
EPOCH ::: 8
Training Net: 100% 137/137 [00:01<00:00, 127.87it/s, Loss_pi=8.38e-01, Loss_v=2.53e-01]
EPOCH ::: 9
Training Net: 100% 137/137 [00:01<00:00, 125.20it/s, Loss_pi=8.09e-01, Loss_v=2.45e-01]
EPOCH ::: 10
Training Net: 100% 137/137 [00:01<00:00, 125.96it/s, Loss_pi=7.92e-01, Loss_v=2.38e-01]
2024-05-16 23:00:17 a4eae8bf3f6b Coach[9078] INFO PITTING AGAINST PREVIOUS VERSION
Arena.playGames (1): 100% 20/20 [02:48<00:00,  8.41s/it]
Arena.playGames (2): 100% 20/20 [02:25<00:00,  7.27s/it]
2024-05-16 23:05:31 a4eae8bf3f6b Coach[9078] INFO NEW/PREV WINS : 2 / 3 ; DRAWS : 35
2024-05-16 23:05:31 a4eae8bf3f6b Coach[9078] INFO REJECTING NEW MODEL
2024-05-16 23:05:31 a4eae8bf3f6b Coach[9078] INFO Starting Iter #5 ...
Self Play: 100% 100/100 [14:22<00:00,  8.63s/it]
Checkpoint Directory exists! 
EPOCH ::: 1
Training Net: 100% 171/171 [00:01<00:00, 127.38it/s, Loss_pi=1.05e+00, Loss_v=3.24e-01]
EPOCH ::: 2
Training Net: 100% 171/171 [00:01<00:00, 121.68it/s, Loss_pi=9.68e-01, Loss_v=2.95e-01]
EPOCH ::: 3
Training Net: 100% 171/171 [00:01<00:00, 127.03it/s, Loss_pi=9.20e-01, Loss_v=2.76e-01]
EPOCH ::: 4
Training Net: 100% 171/171 [00:01<00:00, 128.23it/s, Loss_pi=8.89e-01, Loss_v=2.69e-01]
EPOCH ::: 5
Training Net: 100% 171/171 [00:01<00:00, 128.19it/s, Loss_pi=8.52e-01, Loss_v=2.58e-01]
EPOCH ::: 6
Training Net: 100% 171/171 [00:01<00:00, 125.38it/s, Loss_pi=8.34e-01, Loss_v=2.59e-01]
EPOCH ::: 7
Training Net: 100% 171/171 [00:01<00:00, 126.74it/s, Loss_pi=8.14e-01, Loss_v=2.39e-01]
EPOCH ::: 8
Training Net: 100% 171/171 [00:01<00:00, 122.81it/s, Loss_pi=7.91e-01, Loss_v=2.37e-01]
EPOCH ::: 9
Training Net: 100% 171/171 [00:01<00:00, 128.20it/s, Loss_pi=7.78e-01, Loss_v=2.27e-01]
EPOCH ::: 10
Training Net: 100% 171/171 [00:01<00:00, 128.42it/s, Loss_pi=7.57e-01, Loss_v=2.27e-01]
2024-05-16 23:20:08 a4eae8bf3f6b Coach[9078] INFO PITTING AGAINST PREVIOUS VERSION
Arena.playGames (1): 100% 20/20 [02:46<00:00,  8.34s/it]
Arena.playGames (2): 100% 20/20 [02:43<00:00,  8.16s/it]
2024-05-16 23:25:38 a4eae8bf3f6b Coach[9078] INFO NEW/PREV WINS : 1 / 2 ; DRAWS : 37
2024-05-16 23:25:38 a4eae8bf3f6b Coach[9078] INFO REJECTING NEW MODEL
2024-05-16 23:25:38 a4eae8bf3f6b Coach[9078] INFO Starting Iter #6 ...
Self Play: 100% 100/100 [14:36<00:00,  8.77s/it]
Checkpoint Directory exists! 
EPOCH ::: 1
Training Net: 100% 207/207 [00:01<00:00, 130.22it/s, Loss_pi=1.05e+00, Loss_v=2.95e-01]
EPOCH ::: 2
Training Net: 100% 207/207 [00:01<00:00, 125.47it/s, Loss_pi=9.45e-01, Loss_v=2.91e-01]
EPOCH ::: 3
Training Net: 100% 207/207 [00:01<00:00, 124.11it/s, Loss_pi=8.87e-01, Loss_v=2.71e-01]
EPOCH ::: 4
Training Net: 100% 207/207 [00:01<00:00, 128.17it/s, Loss_pi=8.58e-01, Loss_v=2.54e-01]
EPOCH ::: 5
Training Net: 100% 207/207 [00:01<00:00, 129.50it/s, Loss_pi=8.44e-01, Loss_v=2.61e-01]
EPOCH ::: 6
Training Net: 100% 207/207 [00:01<00:00, 125.91it/s, Loss_pi=7.95e-01, Loss_v=2.47e-01]
EPOCH ::: 7
Training Net: 100% 207/207 [00:01<00:00, 125.71it/s, Loss_pi=7.81e-01, Loss_v=2.36e-01]
EPOCH ::: 8
Training Net: 100% 207/207 [00:01<00:00, 128.19it/s, Loss_pi=7.62e-01, Loss_v=2.27e-01]
EPOCH ::: 9
Training Net: 100% 207/207 [00:01<00:00, 128.67it/s, Loss_pi=7.44e-01, Loss_v=2.21e-01]
EPOCH ::: 10
Training Net: 100% 207/207 [00:01<00:00, 122.70it/s, Loss_pi=7.36e-01, Loss_v=2.19e-01]
2024-05-16 23:40:32 a4eae8bf3f6b Coach[9078] INFO PITTING AGAINST PREVIOUS VERSION
Arena.playGames (1): 100% 20/20 [02:27<00:00,  7.37s/it]
Arena.playGames (2): 100% 20/20 [03:10<00:00,  9.53s/it]
2024-05-16 23:46:10 a4eae8bf3f6b Coach[9078] INFO NEW/PREV WINS : 19 / 0 ; DRAWS : 21
2024-05-16 23:46:10 a4eae8bf3f6b Coach[9078] INFO ACCEPTING NEW MODEL
Checkpoint Directory exists! 
Checkpoint Directory exists! 
2024-05-16 23:46:10 a4eae8bf3f6b Coach[9078] INFO Starting Iter #7 ...
Self Play: 100% 100/100 [13:55<00:00,  8.36s/it]
Checkpoint Directory exists! 
EPOCH ::: 1
Training Net: 100% 240/240 [00:01<00:00, 124.04it/s, Loss_pi=7.74e-01, Loss_v=2.11e-01]
EPOCH ::: 2
Training Net: 100% 240/240 [00:01<00:00, 123.57it/s, Loss_pi=7.38e-01, Loss_v=1.97e-01]
EPOCH ::: 3
Training Net: 100% 240/240 [00:01<00:00, 126.95it/s, Loss_pi=7.17e-01, Loss_v=1.93e-01]
EPOCH ::: 4
Training Net: 100% 240/240 [00:01<00:00, 127.27it/s, Loss_pi=7.03e-01, Loss_v=1.85e-01]
EPOCH ::: 5
Training Net: 100% 240/240 [00:01<00:00, 126.66it/s, Loss_pi=6.88e-01, Loss_v=1.83e-01]
EPOCH ::: 6
Training Net: 100% 240/240 [00:01<00:00, 122.96it/s, Loss_pi=6.72e-01, Loss_v=1.79e-01]
EPOCH ::: 7
Training Net: 100% 240/240 [00:01<00:00, 123.14it/s, Loss_pi=6.83e-01, Loss_v=1.77e-01]
EPOCH ::: 8
Training Net: 100% 240/240 [00:01<00:00, 128.48it/s, Loss_pi=6.73e-01, Loss_v=1.79e-01]
EPOCH ::: 9
Training Net: 100% 240/240 [00:01<00:00, 129.98it/s, Loss_pi=6.59e-01, Loss_v=1.69e-01]
EPOCH ::: 10
Training Net: 100% 240/240 [00:01<00:00, 129.24it/s, Loss_pi=6.56e-01, Loss_v=1.62e-01]
2024-05-17 00:00:25 a4eae8bf3f6b Coach[9078] INFO PITTING AGAINST PREVIOUS VERSION
Arena.playGames (1): 100% 20/20 [02:49<00:00,  8.49s/it]
Arena.playGames (2): 100% 20/20 [02:30<00:00,  7.54s/it]
2024-05-17 00:05:46 a4eae8bf3f6b Coach[9078] INFO NEW/PREV WINS : 3 / 2 ; DRAWS : 35
2024-05-17 00:05:46 a4eae8bf3f6b Coach[9078] INFO ACCEPTING NEW MODEL
Checkpoint Directory exists! 
Checkpoint Directory exists! 
2024-05-17 00:05:46 a4eae8bf3f6b Coach[9078] INFO Starting Iter #8 ...
Self Play: 100% 100/100 [12:41<00:00,  7.62s/it]
Checkpoint Directory exists! 
EPOCH ::: 1
Training Net: 100% 273/273 [00:02<00:00, 124.96it/s, Loss_pi=6.74e-01, Loss_v=1.63e-01]
EPOCH ::: 2
Training Net: 100% 273/273 [00:02<00:00, 127.63it/s, Loss_pi=6.74e-01, Loss_v=1.52e-01]
EPOCH ::: 3
Training Net: 100% 273/273 [00:02<00:00, 127.62it/s, Loss_pi=6.58e-01, Loss_v=1.47e-01]
EPOCH ::: 4
Training Net: 100% 273/273 [00:02<00:00, 129.88it/s, Loss_pi=6.45e-01, Loss_v=1.50e-01]
EPOCH ::: 5
Training Net: 100% 273/273 [00:02<00:00, 124.05it/s, Loss_pi=6.41e-01, Loss_v=1.51e-01]
EPOCH ::: 6
Training Net: 100% 273/273 [00:02<00:00, 125.23it/s, Loss_pi=6.41e-01, Loss_v=1.45e-01]
EPOCH ::: 7
Training Net: 100% 273/273 [00:02<00:00, 126.54it/s, Loss_pi=6.33e-01, Loss_v=1.45e-01]
EPOCH ::: 8
Training Net: 100% 273/273 [00:02<00:00, 125.61it/s, Loss_pi=6.21e-01, Loss_v=1.41e-01]
EPOCH ::: 9
Training Net: 100% 273/273 [00:02<00:00, 128.22it/s, Loss_pi=6.17e-01, Loss_v=1.42e-01]
EPOCH ::: 10
Training Net: 100% 273/273 [00:02<00:00, 128.45it/s, Loss_pi=6.06e-01, Loss_v=1.38e-01]
2024-05-17 00:18:51 a4eae8bf3f6b Coach[9078] INFO PITTING AGAINST PREVIOUS VERSION
Arena.playGames (1): 100% 20/20 [02:47<00:00,  8.36s/it]
Arena.playGames (2): 100% 20/20 [02:19<00:00,  6.99s/it]
2024-05-17 00:23:58 a4eae8bf3f6b Coach[9078] INFO NEW/PREV WINS : 0 / 7 ; DRAWS : 33
2024-05-17 00:23:58 a4eae8bf3f6b Coach[9078] INFO REJECTING NEW MODEL
2024-05-17 00:23:58 a4eae8bf3f6b Coach[9078] INFO Starting Iter #9 ...
Self Play: 100% 100/100 [13:00<00:00,  7.80s/it]
Checkpoint Directory exists! 
EPOCH ::: 1
Training Net: 100% 306/306 [00:02<00:00, 129.39it/s, Loss_pi=7.07e-01, Loss_v=1.60e-01]
EPOCH ::: 2
Training Net: 100% 306/306 [00:02<00:00, 129.25it/s, Loss_pi=6.56e-01, Loss_v=1.50e-01]
EPOCH ::: 3
Training Net: 100% 306/306 [00:02<00:00, 120.69it/s, Loss_pi=6.62e-01, Loss_v=1.52e-01]
EPOCH ::: 4
Training Net: 100% 306/306 [00:02<00:00, 127.27it/s, Loss_pi=6.51e-01, Loss_v=1.43e-01]
EPOCH ::: 5
Training Net: 100% 306/306 [00:02<00:00, 124.50it/s, Loss_pi=6.29e-01, Loss_v=1.40e-01]
EPOCH ::: 6
Training Net: 100% 306/306 [00:02<00:00, 129.86it/s, Loss_pi=6.29e-01, Loss_v=1.40e-01]
EPOCH ::: 7
Training Net: 100% 306/306 [00:02<00:00, 128.45it/s, Loss_pi=6.18e-01, Loss_v=1.35e-01]
EPOCH ::: 8
Training Net: 100% 306/306 [00:02<00:00, 123.25it/s, Loss_pi=6.29e-01, Loss_v=1.37e-01]
EPOCH ::: 9
Training Net: 100% 306/306 [00:02<00:00, 126.42it/s, Loss_pi=6.17e-01, Loss_v=1.31e-01]
EPOCH ::: 10
Training Net: 100% 306/306 [00:02<00:00, 129.56it/s, Loss_pi=6.18e-01, Loss_v=1.35e-01]
2024-05-17 00:37:23 a4eae8bf3f6b Coach[9078] INFO PITTING AGAINST PREVIOUS VERSION
Arena.playGames (1): 100% 20/20 [02:46<00:00,  8.34s/it]
Arena.playGames (2): 100% 20/20 [02:15<00:00,  6.79s/it]
2024-05-17 00:42:25 a4eae8bf3f6b Coach[9078] INFO NEW/PREV WINS : 0 / 3 ; DRAWS : 37
2024-05-17 00:42:25 a4eae8bf3f6b Coach[9078] INFO REJECTING NEW MODEL
2024-05-17 00:42:25 a4eae8bf3f6b Coach[9078] INFO Starting Iter #10 ...
Self Play: 100% 100/100 [12:43<00:00,  7.64s/it]
Checkpoint Directory exists! 
EPOCH ::: 1
Training Net: 100% 339/339 [00:02<00:00, 130.25it/s, Loss_pi=7.06e-01, Loss_v=1.62e-01]
EPOCH ::: 2
Training Net: 100% 339/339 [00:02<00:00, 126.57it/s, Loss_pi=6.72e-01, Loss_v=1.48e-01]
EPOCH ::: 3
Training Net: 100% 339/339 [00:02<00:00, 126.72it/s, Loss_pi=6.49e-01, Loss_v=1.46e-01]
EPOCH ::: 4
Training Net: 100% 339/339 [00:02<00:00, 126.55it/s, Loss_pi=6.45e-01, Loss_v=1.44e-01]
EPOCH ::: 5
Training Net: 100% 339/339 [00:02<00:00, 128.11it/s, Loss_pi=6.36e-01, Loss_v=1.40e-01]
EPOCH ::: 6
Training Net: 100% 339/339 [00:02<00:00, 128.46it/s, Loss_pi=6.28e-01, Loss_v=1.37e-01]
EPOCH ::: 7
Training Net: 100% 339/339 [00:02<00:00, 122.70it/s, Loss_pi=6.24e-01, Loss_v=1.36e-01]
EPOCH ::: 8
Training Net: 100% 339/339 [00:02<00:00, 128.53it/s, Loss_pi=6.08e-01, Loss_v=1.38e-01]
EPOCH ::: 9
Training Net: 100% 339/339 [00:02<00:00, 128.97it/s, Loss_pi=6.07e-01, Loss_v=1.31e-01]
EPOCH ::: 10
Training Net: 100% 339/339 [00:02<00:00, 131.25it/s, Loss_pi=6.06e-01, Loss_v=1.31e-01]
2024-05-17 00:55:37 a4eae8bf3f6b Coach[9078] INFO PITTING AGAINST PREVIOUS VERSION
Arena.playGames (1): 100% 20/20 [02:22<00:00,  7.14s/it]
Arena.playGames (2): 100% 20/20 [02:27<00:00,  7.39s/it]
2024-05-17 01:00:28 a4eae8bf3f6b Coach[9078] INFO NEW/PREV WINS : 0 / 1 ; DRAWS : 39
2024-05-17 01:00:28 a4eae8bf3f6b Coach[9078] INFO REJECTING NEW MODEL
2024-05-17 01:00:28 a4eae8bf3f6b Coach[9078] INFO Starting Iter #11 ...
Self Play:  23% 23/100 [03:11<10:09,  7.92s/it]
EPOCH ::: 1
Training Net: 100% 503/503 [00:05<00:00, 87.61it/s, Loss_pi=7.21e-01, Loss_v=1.30e-01] 
EPOCH ::: 2
Training Net: 100% 503/503 [00:03<00:00, 129.45it/s, Loss_pi=6.64e-01, Loss_v=1.16e-01]
EPOCH ::: 3
Training Net: 100% 503/503 [00:03<00:00, 134.24it/s, Loss_pi=6.57e-01, Loss_v=1.19e-01]
EPOCH ::: 4
Training Net: 100% 503/503 [00:03<00:00, 134.61it/s, Loss_pi=6.31e-01, Loss_v=1.13e-01]
EPOCH ::: 5
Training Net: 100% 503/503 [00:03<00:00, 131.45it/s, Loss_pi=6.10e-01, Loss_v=1.11e-01]
EPOCH ::: 6
Training Net: 100% 503/503 [00:03<00:00, 132.73it/s, Loss_pi=6.07e-01, Loss_v=1.09e-01]
EPOCH ::: 7
Training Net: 100% 503/503 [00:03<00:00, 134.78it/s, Loss_pi=6.01e-01, Loss_v=1.07e-01]
EPOCH ::: 8
Training Net: 100% 503/503 [00:03<00:00, 127.20it/s, Loss_pi=5.92e-01, Loss_v=1.03e-01]
EPOCH ::: 9
Training Net: 100% 503/503 [00:03<00:00, 132.13it/s, Loss_pi=5.92e-01, Loss_v=1.03e-01]
EPOCH ::: 10
Training Net: 100% 503/503 [00:03<00:00, 135.96it/s, Loss_pi=5.83e-01, Loss_v=9.87e-02]
2024-05-20 08:30:37 44c5c2a0ecd3 Coach[3561] INFO PITTING AGAINST PREVIOUS VERSION
Arena.playGames (1): 100% 20/20 [02:36<00:00,  7.84s/it]
Arena.playGames (2): 100% 20/20 [02:18<00:00,  6.92s/it]
2024-05-20 08:35:32 44c5c2a0ecd3 Coach[3561] INFO NEW/PREV WINS : 1 / 0 ; DRAWS : 39
2024-05-20 08:35:32 44c5c2a0ecd3 Coach[3561] INFO ACCEPTING NEW MODEL
Checkpoint Directory exists! 
Checkpoint Directory exists! 
2024-05-20 08:35:37 44c5c2a0ecd3 Coach[3561] INFO Starting Iter #2 ...
Self Play: 100% 100/100 [12:40<00:00,  7.60s/it]
Checkpoint Directory exists! 
EPOCH ::: 1
Training Net: 100% 536/536 [00:04<00:00, 130.04it/s, Loss_pi=5.99e-01, Loss_v=1.01e-01]
EPOCH ::: 2
Training Net: 100% 536/536 [00:04<00:00, 131.28it/s, Loss_pi=5.82e-01, Loss_v=9.28e-02]
EPOCH ::: 3
Training Net: 100% 536/536 [00:04<00:00, 124.86it/s, Loss_pi=5.79e-01, Loss_v=9.62e-02]
EPOCH ::: 4
Training Net: 100% 536/536 [00:04<00:00, 132.58it/s, Loss_pi=5.68e-01, Loss_v=9.43e-02]
EPOCH ::: 5
Training Net: 100% 536/536 [00:04<00:00, 132.23it/s, Loss_pi=5.71e-01, Loss_v=9.77e-02]
EPOCH ::: 6
Training Net: 100% 536/536 [00:04<00:00, 123.66it/s, Loss_pi=5.63e-01, Loss_v=9.09e-02]
EPOCH ::: 7
Training Net: 100% 536/536 [00:04<00:00, 128.35it/s, Loss_pi=5.61e-01, Loss_v=9.37e-02]
EPOCH ::: 8
Training Net: 100% 536/536 [00:04<00:00, 131.85it/s, Loss_pi=5.63e-01, Loss_v=8.91e-02]
EPOCH ::: 9
Training Net: 100% 536/536 [00:04<00:00, 128.76it/s, Loss_pi=5.48e-01, Loss_v=8.63e-02]
EPOCH ::: 10
Training Net: 100% 536/536 [00:04<00:00, 126.24it/s, Loss_pi=5.48e-01, Loss_v=9.09e-02]
2024-05-20 08:49:01 44c5c2a0ecd3 Coach[3561] INFO PITTING AGAINST PREVIOUS VERSION
Arena.playGames (1): 100% 20/20 [02:16<00:00,  6.82s/it]
Arena.playGames (2): 100% 20/20 [02:36<00:00,  7.82s/it]
2024-05-20 08:53:54 44c5c2a0ecd3 Coach[3561] INFO NEW/PREV WINS : 0 / 2 ; DRAWS : 38
2024-05-20 08:53:54 44c5c2a0ecd3 Coach[3561] INFO REJECTING NEW MODEL
2024-05-20 08:53:54 44c5c2a0ecd3 Coach[3561] INFO Starting Iter #3 ...
Self Play: 100% 100/100 [12:33<00:00,  7.53s/it]
Checkpoint Directory exists! 
EPOCH ::: 1
Training Net: 100% 569/569 [00:04<00:00, 129.53it/s, Loss_pi=5.91e-01, Loss_v=9.98e-02]
EPOCH ::: 2
Training Net: 100% 569/569 [00:04<00:00, 128.33it/s, Loss_pi=5.83e-01, Loss_v=9.80e-02]
EPOCH ::: 3
Training Net: 100% 569/569 [00:04<00:00, 125.59it/s, Loss_pi=5.68e-01, Loss_v=9.34e-02]
EPOCH ::: 4
Training Net: 100% 569/569 [00:04<00:00, 127.49it/s, Loss_pi=5.70e-01, Loss_v=9.09e-02]
EPOCH ::: 5
Training Net: 100% 569/569 [00:04<00:00, 128.67it/s, Loss_pi=5.58e-01, Loss_v=9.18e-02]
EPOCH ::: 6
Training Net: 100% 569/569 [00:04<00:00, 125.22it/s, Loss_pi=5.62e-01, Loss_v=9.19e-02]
EPOCH ::: 7
Training Net: 100% 569/569 [00:04<00:00, 131.16it/s, Loss_pi=5.62e-01, Loss_v=9.13e-02]
EPOCH ::: 8
Training Net: 100% 569/569 [00:04<00:00, 130.60it/s, Loss_pi=5.59e-01, Loss_v=8.92e-02]
EPOCH ::: 9
Training Net: 100% 569/569 [00:04<00:00, 127.64it/s, Loss_pi=5.53e-01, Loss_v=8.78e-02]
EPOCH ::: 10
Training Net: 100% 569/569 [00:04<00:00, 131.27it/s, Loss_pi=5.50e-01, Loss_v=8.76e-02]
2024-05-20 09:07:14 44c5c2a0ecd3 Coach[3561] INFO PITTING AGAINST PREVIOUS VERSION
Arena.playGames (1): 100% 20/20 [02:11<00:00,  6.59s/it]
Arena.playGames (2): 100% 20/20 [02:33<00:00,  7.69s/it]
2024-05-20 09:11:59 44c5c2a0ecd3 Coach[3561] INFO NEW/PREV WINS : 4 / 2 ; DRAWS : 34
2024-05-20 09:11:59 44c5c2a0ecd3 Coach[3561] INFO ACCEPTING NEW MODEL
Checkpoint Directory exists! 
Checkpoint Directory exists! 
2024-05-20 09:12:02 44c5c2a0ecd3 Coach[3561] INFO Starting Iter #4 ...
Self Play: 100% 100/100 [12:20<00:00,  7.41s/it]
Checkpoint Directory exists! 
EPOCH ::: 1
Training Net: 100% 602/602 [00:04<00:00, 129.71it/s, Loss_pi=5.55e-01, Loss_v=8.60e-02]
EPOCH ::: 2
Training Net: 100% 602/602 [00:04<00:00, 125.75it/s, Loss_pi=5.56e-01, Loss_v=8.48e-02]
EPOCH ::: 3
Training Net: 100% 602/602 [00:04<00:00, 122.77it/s, Loss_pi=5.45e-01, Loss_v=8.30e-02]
EPOCH ::: 4
Training Net: 100% 602/602 [00:04<00:00, 129.91it/s, Loss_pi=5.46e-01, Loss_v=8.63e-02]
EPOCH ::: 5
Training Net: 100% 602/602 [00:04<00:00, 129.38it/s, Loss_pi=5.40e-01, Loss_v=8.62e-02]
EPOCH ::: 6
Training Net: 100% 602/602 [00:04<00:00, 128.21it/s, Loss_pi=5.47e-01, Loss_v=8.33e-02]
EPOCH ::: 7
Training Net: 100% 602/602 [00:04<00:00, 126.01it/s, Loss_pi=5.34e-01, Loss_v=8.15e-02]
EPOCH ::: 8
Training Net: 100% 602/602 [00:04<00:00, 132.14it/s, Loss_pi=5.39e-01, Loss_v=8.11e-02]
EPOCH ::: 9
Training Net: 100% 602/602 [00:04<00:00, 129.25it/s, Loss_pi=5.35e-01, Loss_v=8.18e-02]
EPOCH ::: 10
Training Net: 100% 602/602 [00:04<00:00, 126.92it/s, Loss_pi=5.35e-01, Loss_v=7.99e-02]
2024-05-20 09:25:12 44c5c2a0ecd3 Coach[3561] INFO PITTING AGAINST PREVIOUS VERSION
Arena.playGames (1): 100% 20/20 [02:04<00:00,  6.24s/it]
Arena.playGames (2): 100% 20/20 [01:59<00:00,  5.97s/it]
2024-05-20 09:29:16 44c5c2a0ecd3 Coach[3561] INFO NEW/PREV WINS : 0 / 0 ; DRAWS : 40
2024-05-20 09:29:16 44c5c2a0ecd3 Coach[3561] INFO REJECTING NEW MODEL
2024-05-20 09:29:16 44c5c2a0ecd3 Coach[3561] INFO Starting Iter #5 ...
Self Play: 100% 100/100 [12:23<00:00,  7.43s/it]
Checkpoint Directory exists! 
EPOCH ::: 1
Training Net: 100% 635/635 [00:05<00:00, 124.92it/s, Loss_pi=5.60e-01, Loss_v=8.49e-02]
EPOCH ::: 2
Training Net: 100% 635/635 [00:05<00:00, 126.31it/s, Loss_pi=5.46e-01, Loss_v=8.50e-02]
EPOCH ::: 3
Training Net: 100% 635/635 [00:05<00:00, 126.07it/s, Loss_pi=5.45e-01, Loss_v=8.45e-02]
EPOCH ::: 4
Training Net: 100% 635/635 [00:04<00:00, 127.57it/s, Loss_pi=5.39e-01, Loss_v=8.24e-02]
EPOCH ::: 5
Training Net: 100% 635/635 [00:04<00:00, 129.01it/s, Loss_pi=5.39e-01, Loss_v=8.27e-02]
EPOCH ::: 6
Training Net: 100% 635/635 [00:05<00:00, 126.07it/s, Loss_pi=5.37e-01, Loss_v=8.04e-02]
EPOCH ::: 7
Training Net: 100% 635/635 [00:04<00:00, 129.47it/s, Loss_pi=5.40e-01, Loss_v=8.18e-02]
EPOCH ::: 8
Training Net: 100% 635/635 [00:04<00:00, 128.36it/s, Loss_pi=5.33e-01, Loss_v=7.93e-02]
EPOCH ::: 9
Training Net: 100% 635/635 [00:04<00:00, 127.56it/s, Loss_pi=5.34e-01, Loss_v=7.93e-02]
EPOCH ::: 10
Training Net: 100% 635/635 [00:04<00:00, 130.12it/s, Loss_pi=5.30e-01, Loss_v=7.61e-02]
2024-05-20 09:42:32 44c5c2a0ecd3 Coach[3561] INFO PITTING AGAINST PREVIOUS VERSION
Arena.playGames (1): 100% 20/20 [01:54<00:00,  5.71s/it]
Arena.playGames (2): 100% 20/20 [01:54<00:00,  5.73s/it]
2024-05-20 09:46:21 44c5c2a0ecd3 Coach[3561] INFO NEW/PREV WINS : 0 / 0 ; DRAWS : 40
2024-05-20 09:46:21 44c5c2a0ecd3 Coach[3561] INFO REJECTING NEW MODEL
2024-05-20 09:46:21 44c5c2a0ecd3 Coach[3561] INFO Starting Iter #6 ...
Self Play: 100% 100/100 [12:00<00:00,  7.21s/it]
Checkpoint Directory exists! 
EPOCH ::: 1
Training Net: 100% 667/667 [00:05<00:00, 128.00it/s, Loss_pi=5.65e-01, Loss_v=8.57e-02]
EPOCH ::: 2
Training Net: 100% 667/667 [00:05<00:00, 125.59it/s, Loss_pi=5.48e-01, Loss_v=7.99e-02]
EPOCH ::: 3
Training Net: 100% 667/667 [00:05<00:00, 130.84it/s, Loss_pi=5.44e-01, Loss_v=8.32e-02]
EPOCH ::: 4
Training Net: 100% 667/667 [00:05<00:00, 128.44it/s, Loss_pi=5.34e-01, Loss_v=8.01e-02]
EPOCH ::: 5
Training Net: 100% 667/667 [00:05<00:00, 124.59it/s, Loss_pi=5.39e-01, Loss_v=8.02e-02]
EPOCH ::: 6
Training Net: 100% 667/667 [00:05<00:00, 128.02it/s, Loss_pi=5.30e-01, Loss_v=7.86e-02]
EPOCH ::: 7
Training Net: 100% 667/667 [00:05<00:00, 128.33it/s, Loss_pi=5.37e-01, Loss_v=7.75e-02]
EPOCH ::: 8
Training Net: 100% 667/667 [00:05<00:00, 131.77it/s, Loss_pi=5.34e-01, Loss_v=7.94e-02]
EPOCH ::: 9
Training Net: 100% 667/667 [00:05<00:00, 125.79it/s, Loss_pi=5.26e-01, Loss_v=7.83e-02]
EPOCH ::: 10
Training Net: 100% 667/667 [00:05<00:00, 129.08it/s, Loss_pi=5.28e-01, Loss_v=7.80e-02]
2024-05-20 09:59:16 44c5c2a0ecd3 Coach[3561] INFO PITTING AGAINST PREVIOUS VERSION
Arena.playGames (1): 100% 20/20 [01:54<00:00,  5.71s/it]
Arena.playGames (2): 100% 20/20 [01:55<00:00,  5.79s/it]
2024-05-20 10:03:07 44c5c2a0ecd3 Coach[3561] INFO NEW/PREV WINS : 0 / 0 ; DRAWS : 40
2024-05-20 10:03:07 44c5c2a0ecd3 Coach[3561] INFO REJECTING NEW MODEL
2024-05-20 10:03:07 44c5c2a0ecd3 Coach[3561] INFO Starting Iter #7 ...
Self Play: 100% 100/100 [12:05<00:00,  7.25s/it]
2024-05-20 10:15:12 44c5c2a0ecd3 Coach[3561] WARNING Removing the oldest entry in trainExamples. len(trainExamplesHistory) = 21
Checkpoint Directory exists! 
EPOCH ::: 1
Training Net: 100% 671/671 [00:05<00:00, 127.91it/s, Loss_pi=5.35e-01, Loss_v=7.58e-02]
EPOCH ::: 2
Training Net: 100% 671/671 [00:05<00:00, 121.53it/s, Loss_pi=5.18e-01, Loss_v=7.55e-02]
EPOCH ::: 3
Training Net: 100% 671/671 [00:05<00:00, 124.57it/s, Loss_pi=5.09e-01, Loss_v=7.41e-02]
EPOCH ::: 4
Training Net: 100% 671/671 [00:05<00:00, 126.62it/s, Loss_pi=5.09e-01, Loss_v=7.01e-02]
EPOCH ::: 5
Training Net: 100% 671/671 [00:05<00:00, 126.98it/s, Loss_pi=5.07e-01, Loss_v=7.37e-02]
EPOCH ::: 6
Training Net: 100% 671/671 [00:05<00:00, 130.06it/s, Loss_pi=5.02e-01, Loss_v=6.94e-02]
EPOCH ::: 7
Training Net: 100% 671/671 [00:05<00:00, 126.20it/s, Loss_pi=5.00e-01, Loss_v=7.01e-02]
EPOCH ::: 8
Training Net: 100% 671/671 [00:05<00:00, 128.16it/s, Loss_pi=5.05e-01, Loss_v=6.96e-02]
EPOCH ::: 9
Training Net: 100% 671/671 [00:05<00:00, 124.72it/s, Loss_pi=4.98e-01, Loss_v=6.92e-02]
EPOCH ::: 10
Training Net: 100% 671/671 [00:05<00:00, 127.15it/s, Loss_pi=5.00e-01, Loss_v=7.07e-02]
2024-05-20 10:16:08 44c5c2a0ecd3 Coach[3561] INFO PITTING AGAINST PREVIOUS VERSION
Arena.playGames (1): 100% 20/20 [01:54<00:00,  5.71s/it]
Arena.playGames (2): 100% 20/20 [01:55<00:00,  5.78s/it]
2024-05-20 10:19:57 44c5c2a0ecd3 Coach[3561] INFO NEW/PREV WINS : 0 / 0 ; DRAWS : 40
2024-05-20 10:19:57 44c5c2a0ecd3 Coach[3561] INFO REJECTING NEW MODEL
2024-05-20 10:19:57 44c5c2a0ecd3 Coach[3561] INFO Starting Iter #8 ...
Self Play:  37% 37/100 [04:24<07:30,  7.16s/it]
'''

# Regex pattern to capture Loss_pi and Loss_v values
pattern = r'Loss_pi=([\d.e+-]+), Loss_v=([\d.e+-]+)'

# Finding all matches in the data
losses = re.findall(pattern, data)

# Splitting the results into separate lists for Loss_pi and Loss_v
loss_pi = [float(pi) for pi, _ in losses]
loss_v = [float(v) for _, v in losses]

# Plotting Loss_pi
plt.figure(figsize=(10, 5))
plt.plot(loss_pi, label='Loss_pi', marker=',')
plt.title('Loss_pi over Epochs')
plt.xlabel('Epoch')
plt.ylabel('Loss_pi')
plt.grid(True)
plt.legend()
plt.show()

# Plotting Loss_v
plt.figure(figsize=(10, 5))
plt.plot(loss_v, label='Loss_v', marker=',', color='red')
plt.title('Loss_v over Epochs')
plt.xlabel('Epoch')
plt.ylabel('Loss_v')
plt.grid(True)
plt.legend()
plt.show()

# Plotting Loss_pi and Loss_v on the same graph
plt.figure(figsize=(10, 5))
plt.plot(loss_pi, label='Loss_pi', marker=',')
plt.plot(loss_v, label='Loss_v', marker=',', color='red')
plt.title('Loss_pi and Loss_v over Epochs')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.grid(True)
plt.legend()
plt.show()