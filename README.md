# ValeroArm
I spent the summer of 2019 building a cost-effective, durable, and versatile tendon-driven arm. The motivation was to build an arm that had planar, universal, and rotational joints on a large scale. This design could then be scaled down to the size of fingers on the hand. We built and modled a planar, two joint, three muscle system.

# Tendon Routing and Moment Arm Size Optimization
  A large focus was directed toward finding the optimal tendon routing for the arm. This was done in python by maximizing the radius of a circle inside the Feasible Force Set with the circle’s center located at the endpoint. The choice of a circle defined the maximum force the endpoint could exert in all directions. The routes with the highest radii over the entire sweep of the joint were determined to be the most versatile. We defined versatile as “producing the largest force in all directions, for every position.”
  
  For a two joint, three muscle this produces a 2x3 matrix with close to 800 combinations. Each row is a joint and each column is a muscle. The numbers one and negative one were used to denote the direction of angle change that a tendon could produce. Tendons can only act on a joint in one direction because muscles only contract and cannot extend. The possible R matrices were reduced to 14 by the following assumptions: 
    
    1.	Every row needs a positive and negative moment arm to move in both directions.
    2.	The top row cannot contain a zero because the current design of the arm does not 
        allow a tendon to reach the distal  joint without first touching the proximal joint. 
    3.	Matrices with the same columns in different orders are duplicates of each other. 
    
  Out of the 14 matrices, 10 produced numerical results with 2 routes clearly stronger than the rest. These two matrices were “opposites” of each other as shown in FIGURE. This optimal tendon routing is consistent with the routing chosen in (G2P Paper). This information was presented on a poster at the Keck School of Medicine’s summer undergraduate poster symposium. 
	
  The 14 feasible routes were then scaled to allow for moment arm differences between each muscle and joints. The 14 feasible routes were multiplied by almost 2 million scaling matrices by scalar multiplication.  These scaling matrices were all the variations of a 2x3 matrix containing the numbers between 0 and 1 (inclusive) with a 0.1 step (0,0.1,0.2,0.3…). By choosing a maximum of 1.0, these values are normalized by dividing all the values by the arm's largest moment arm. These new scaling matrices were ran through the same optimization procedure as before. 

# Physical Design and Construction
  The first design of the arm was constructed together with Paris Hijali. It was made out of PVC and 3D printed components. While it was a solid proof of concept, there were many problems that arose. I addressed many of these problems in the second version. 
  
  Version 2 was created using very modular parts which allowed for the arm to be modified depending on the task. Most of the parts were ordered from McMaster or ServoCity. This version of the arm included a planar elbow and shoulder joint along with a rotational pronation/supination joint in the forearm. At the end of the arm, there were three versions of a wrist-- ranging from zero to the two degrees of freedom that a real wrist has. We constructed the version with zero DOFs for the first phase of testing. The current hand we were using in the lab was underactuated and driven by two servos. There was a cavity created in the distal forearm to house the two servos needed to drive the hand. 
