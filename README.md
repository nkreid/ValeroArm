# ValeroArm
I spent the summer of 2019 building a cost-effective, durable, and versatile tendon-driven arm. The motivation was to build an arm that had planar, universal, and rotational joints on a large scale. This design could then be scaled down to the size of fingers on the hand. We built and modled a planar, two joint, three muscle system.

# Tendon Routing and Moment Arm Size Optimization
  A large focus was directed toward finding the optimal tendon routing for the arm. This was done in python by maximizing the radius of a circle inside the Feasible Force Set with the circle’s center located at the endpoint. The choice of a circle defined the maximum force the endpoint could exert in all directions. The routes were sweeped over the anotmical limits of the elbow (-10 degrees,150 degrees) and averaged over the range. This average force production was our metric we used to pick the most versatile route. We defined versatile as “producing the largest force in all directions, for every position.”
  
  For a two joint, three muscle this produces a 2x3 matrix with close to 800 combinations. Each row is a joint and each column is a muscle. The numbers one and negative one were used to denote the direction of angle change that a tendon could produce. Tendons can only act on a joint in one direction because muscles only contract and cannot extend. The possible R matrices were reduced to 14 by the following assumptions: 
    
    1.	Every row needs a positive and negative moment arm to move in both directions.
    2.	The top row cannot contain a zero because the current design of the arm does not 
        allow a tendon to reach the distal  joint without first touching the proximal joint. 
    3.	Matrices with the same columns in different orders are duplicates of each other. 
    
  Out of the 14 matrices, 10 produced numerical results with 2 routes clearly stronger than the rest. These two matrices were “opposites” of each other as shown in FIGURE. This optimal tendon routing is consistent with the routing chosen in (G2P Paper). This information was presented on a poster at the Keck School of Medicine’s summer undergraduate poster symposium. 
	
  The 14 feasible routes were then scaled to allow for moment arm differences between each muscle and joints. The 14 feasible routes were multiplied by almost 2 million scaling matrices by scalar multiplication.  These scaling matrices were all the variations of a 2x3 matrix containing the numbers between 0 and 1 (inclusive) with a 0.1 step (0,0.1,0.2,0.3…). By choosing a maximum of 1.0, these values are normalized by dividing all the values by the arm's largest moment arm. These new matrices were ran through the same optimization procedure as before and the top 100 matrices were kept. The results are as follows:
```
       MATRIX         Average Force Output
[[-1.   0.2  0.9]
 [-0.1 -1.   1. ]]  :: 2.3684792518615723
[[-1.   1.   0.4]
 [-0.6 -0.9  1. ]]  :: 2.369333267211914
[[-1.   0.9  0.4]
 [-0.6 -0.8  1. ]]  :: 2.369748115539551
[[-0.1 -0.9  1. ]
 [-1.   0.3  0.6]]  :: 2.3703784942626953
[[-1.  -0.1  1. ]
 [-1.   0.9  0.1]]  :: 2.3703880310058594
[[-0.1 -1.   1. ]
 [-1.   0.2  0.9]]  :: 2.3708009719848633
[[-1.   1.   0.1]
 [-1.  -0.5  1. ]]  :: 2.373188018798828
[[-0.1 -1.   1. ]
 [-1.   0.3  0.6]]  :: 2.376481533050537
[[-1.  -0.1  1. ]
 [-1.   1.   0.1]]  :: 2.3765554428100586
[[-1.   0.9  0.1]
 [-0.8 -0.5  1. ]]  :: 2.377281665802002
[[-1.   1.   0.2]
 [-0.8 -0.3  1. ]]  :: 2.377704620361328
[[-1.   0.1  1. ]
 [-0.1 -1.   0.9]]  :: 2.3780016899108887
[[-1.   0.1  1. ]
 [-0.2 -0.9  1. ]]  :: 2.3781371116638184
[[-1.   1.   0.2]
 [-0.6 -0.6  1. ]]  :: 2.37845516204834
[[-0.1 -1.   1. ]
 [-1.   0.3  0.7]]  :: 2.3785605430603027
[[-0.1 -0.9  1. ]
 [-1.   0.   0.9]]  :: 2.378894805908203
[[-1.   0.8  0.2]
 [-0.8 -0.4  1. ]]  :: 2.378972053527832
[[-1.   1.   0.2]
 [-0.8 -0.5  1. ]]  :: 2.378972053527832
[[-1.   1.   0.2]
 [-0.7 -0.4  1. ]]  :: 2.380239963531494
[[-1.   0.8  0.2]
 [-0.8 -0.3  1. ]]  :: 2.380913734436035
[[-1.   0.7  0.3]
 [-0.6 -0.5  1. ]]  :: 2.3826379776000977
[[-1.   1.   0.3]
 [-0.6 -0.7  1. ]]  :: 2.382941246032715
[[-1.   0.9  0.1]
 [-0.9 -0.2  0.9]]  :: 2.3833484649658203
[[-0.1 -0.9  1. ]
 [-1.   0.1  0.9]]  :: 2.384080410003662
[[-1.   0.9  0.1]
 [-0.9 -0.1  1. ]]  :: 2.384080410003662
[[-1.   0.9  0.2]
 [-0.8 -0.3  1. ]]  :: 2.3842296600341797
[[-1.   0.1  1. ]
 [-0.2 -1.   1. ]]  :: 2.3846397399902344
[[-1.   0.8  0.2]
 [-0.6 -0.5  1. ]]  :: 2.3851661682128906
[[-0.1 -1.   1. ]
 [-1.   0.1  0.9]]  :: 2.3852338790893555
[[-1.  -0.1  1. ]
 [-0.9  1.  -0.1]]  :: 2.385453224182129
[[-1.   1.   0.1]
 [-0.8 -0.3  0.9]]  :: 2.385678291320801
[[-1.   0.8  0.2]
 [-0.7 -0.5  1. ]]  :: 2.3862833976745605
[[-1.   0.9  0.2]
 [-0.6 -0.6  1. ]]  :: 2.386333465576172
[[-1.   0.9  0.1]
 [-0.9 -0.1  0.9]]  :: 2.3866147994995117
[[-0.1 -1.   1. ]
 [-1.   0.   0.9]]  :: 2.386654853820801
[[-1.   0.9  0.3]
 [-0.6 -0.7  1. ]]  :: 2.3869214057922363
[[-1.   1.   0.1]
 [-0.8 -0.2  0.9]]  :: 2.387248992919922
[[-1.   1.   0.1]
 [-0.9 -0.2  0.9]]  :: 2.3876848220825195
[[-1.   0.9  0.2]
 [-0.8 -0.4  1. ]]  :: 2.3879594802856445
[[-0.1 -0.9  1. ]
 [-1.   0.2  0.8]]  :: 2.388108730316162
[[-1.   0.9  0.1]
 [-0.8 -0.2  1. ]]  :: 2.388108730316162
[[-1.   0.9  0.1]
 [-0.7 -0.5  1. ]]  :: 2.3896474838256836
[[-1.   1.   0.1]
 [-0.9 -0.5  1. ]]  :: 2.389890670776367
[[-1.   0.8  0.3]
 [-0.6 -0.6  1. ]]  :: 2.3907508850097656
[[-1.   1.   0.1]
 [-0.9 -0.1  0.9]]  :: 2.391145706176758
[[-0.9 -0.1  1. ]
 [-0.9  1.  -0.2]]  :: 2.3913187980651855
[[-1.   0.9  0.1]
 [-0.8 -0.2  0.9]]  :: 2.391659736633301
[[-1.   0.9  0.1]
 [-1.  -0.4  1. ]]  :: 2.3922195434570312
[[-1.   1.   0.2]
 [-0.8 -0.4  1. ]]  :: 2.392786979675293
[[-0.1 -1.   1. ]
 [-1.   0.2  0.8]]  :: 2.3943839073181152
[[-1.   1.   0.1]
 [-0.8 -0.2  1. ]]  :: 2.395249843597412
[[-1.   1.   0.2]
 [-0.7 -0.6  1. ]]  :: 2.3952860832214355
[[-1.   0.9  0.2]
 [-0.7 -0.4  1. ]]  :: 2.3953776359558105
[[-0.1 -0.9  1. ]
 [-1.   0.2  0.7]]  :: 2.3994054794311523
[[-1.  -0.1  1. ]
 [-0.9  1.  -0.2]]  :: 2.400559902191162
[[-0.9 -0.1  1. ]
 [-1.   1.  -0.2]]  :: 2.4009556770324707
[[-1.  -0.1  1. ]
 [-1.   1.  -0.2]]  :: 2.4009556770324707
[[-1.   0.1  0.9]
 [ 0.  -1.   0.9]]  :: 2.402737617492676
[[-0.1 -1.   1. ]
 [-1.   0.2  0.7]]  :: 2.4031448364257812
[[-1.   0.8  0.2]
 [-0.7 -0.4  1. ]]  :: 2.403982639312744
[[-1.   1.   0.1]
 [-1.  -0.4  1. ]]  :: 2.4048118591308594
[[-1.   1.   0.1]
 [-0.8 -0.5  1. ]]  :: 2.4048967361450195
[[-1.   0.1  0.9]
 [-0.2 -0.9  1. ]]  :: 2.4055685997009277
[[-0.1 -0.9  1. ]
 [-1.   0.1  0.8]]  :: 2.405982494354248
[[-1.   0.1  1. ]
 [ 0.  -1.   0.9]]  :: 2.4064602851867676
[[-1.   0.1  0.9]
 [-0.2 -1.   1. ]]  :: 2.4069385528564453
[[-1.   1.   0.1]
 [-0.7 -0.4  1. ]]  :: 2.408623218536377
[[-1.   0.9  0.2]
 [-0.7 -0.5  1. ]]  :: 2.409496784210205
[[-0.9 -0.1  1. ]
 [-1.   1.   0. ]]  :: 2.4098424911499023
[[-1.   0.1  0.9]
 [ 0.  -1.   1. ]]  :: 2.4098424911499023
[[-1.   0.1  1. ]
 [ 0.  -1.   1. ]]  :: 2.410043716430664
[[-1.   1.   0.2]
 [-0.7 -0.5  1. ]]  :: 2.4102797508239746
[[-0.9 -0.1  1. ]
 [-1.   0.9  0. ]]  :: 2.4110989570617676
[[-1.   0.9  0.1]
 [-0.9 -0.4  1. ]]  :: 2.411163330078125
[[-1.   1.   0.1]
 [-0.9 -0.1  1. ]]  :: 2.414584159851074
[[-0.1 -1.   1. ]
 [-1.   0.1  0.8]]  :: 2.415041446685791
[[-1.  -0.1  1. ]
 [-1.   0.9  0. ]]  :: 2.415407657623291
[[-1.   1.   0.1]
 [-0.7 -0.5  1. ]]  :: 2.4193854331970215
[[-1.   0.9  0.1]
 [-1.  -0.3  1. ]]  :: 2.419833183288574
[[-1.   1.   0.1]
 [-1.   0.   1. ]]  :: 2.4215126037597656
[[-1.   0.9  0.1]
 [-0.7 -0.4  1. ]]  :: 2.422842025756836
[[-1.   1.   0.1]
 [-0.9 -0.4  1. ]]  :: 2.4256467819213867
[[-1.   1.   0.1]
 [-1.  -0.3  1. ]]  :: 2.4256591796875
[[-1.   0.9  0.1]
 [-1.  -0.1  1. ]]  :: 2.4260425567626953
[[-1.  -0.1  1. ]
 [-1.   1.   0. ]]  :: 2.4276933670043945
[[-1.   0.9  0.1]
 [-0.8 -0.4  1. ]]  :: 2.4277634620666504
[[-1.   0.9  0.1]
 [-1.  -0.2  1. ]]  :: 2.434298515319824
[[-1.   1.   0.1]
 [-1.  -0.2  1. ]]  :: 2.4354095458984375
[[-1.   1.   0.1]
 [-1.  -0.1  1. ]]  :: 2.43552303314209
[[-0.9 -0.1  1. ]
 [-1.   1.  -0.1]]  :: 2.439504623413086
[[-1.   0.1  1. ]
 [-0.1 -1.   1. ]]  :: 2.440884590148926
[[-1.   1.   0.1]
 [-0.8 -0.3  1. ]]  :: 2.4428586959838867
[[-1.   1.   0.1]
 [-0.8 -0.4  1. ]]  :: 2.4435338973999023
[[-1.   0.9  0.1]
 [-0.9 -0.3  1. ]]  :: 2.4436330795288086
[[-1.   0.1  0.9]
 [-0.1 -1.   1. ]]  :: 2.445775032043457
[[-1.  -0.1  1. ]
 [-1.   1.  -0.1]]  :: 2.4461536407470703
[[-1.   0.9  0.1]
 [-0.8 -0.3  1. ]]  :: 2.4498729705810547
[[-1.   1.   0.1]
 [-0.9 -0.3  1. ]]  :: 2.4512014389038086
[[-1.   1.   0.1]
 [-0.9 -0.2  1. ]]  :: 2.4544849395751953
[[-1.   0.9  0.1]
 [-0.9 -0.2  1. ]]  :: 2.4554500579833984
```

It is interesting to note that our best routes are not all ones and zeros as initially exepcted. However, the top 5 results are all very similar with minor deviations.

# Physical Design and Construction
  The first design of the arm was constructed together with Paris Hijali. It was made out of PVC and 3D printed components. While it was a solid proof of concept, there were many problems that arose. I addressed many of these problems in the second version. 
![PVC Arm](/Images/IMG_3504.jpeg)
  Version 2 was created using very modular parts which allowed for the arm to be modified depending on the task. Most of the parts were ordered from McMaster or ServoCity. This version of the arm included a planar elbow and shoulder joint along with a rotational pronation/supination joint in the forearm. At the end of the arm, there were three versions of a wrist-- ranging from zero to the two degrees of freedom that a real wrist has. We constructed the version with zero DOFs for the first phase of testing. The current hand we were using in the lab was underactuated and driven by two servos. There was a cavity created in the distal forearm to house the two servos needed to drive the hand. 
![Modular Arm (Hardware/Renderings/HAND,_servo_break,_0_DOF_wrist_2019-Jul-27_07-49-22PM-000_CustomizedView27924672088_png.png)
  We designed a multi-moment-arm (MMA) for a planar joint. It allowed a multiple tendons to pass over the same joint with different moment arms. If I were to experimentally test the optimization that I presented above, I would create different MMA according to different routes. I would then put the endpoint of the arm into a device to measure the force. I could then sweep the elbow joint and measure the forces in different postures to see if it supports the data derived theoretically. 
