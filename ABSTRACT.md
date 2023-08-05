The **Damage Detection of Power Plants** dataset comprises expert-annotated damages on various types of power plant images, including *Wind Turbine Optical Images*, *Solar Panel Optical Images (Small)*, *Solar Panel Optical Images (Large)*, and *Solar Panel Infrared Images*.

The authors of the dataset are interested in exploring image-based monitoring as a promising and cost-effective solution for large-scale renewable plants. They aim to automate the detection of damages in power installations using drone-acquired images. However, they face challenges such as size and scale variations, variations in light conditions, and the rarity of some damage types, which can make automated detection difficult, particularly for machine learning methods that rely on a large number of examples.

To evaluate their approach, the authors utilized four different datasets, including *Solar Panel Optical Images (Large)* obtained with a DJI Mavic Pro drone, *Wind Turbine Optical Images* captured by professional drone operators in DTU wind energy facilities, *Solar Panel Optical Images (Small)* from the work of Mehta et al. (2018), and *Solar Panel Infrared Images* produced by Alfaro-Mejía et al. (2019). They mixed these datasets to evaluate the performance of deep learning-based object detection models for damage detection across different origins and image sensing modalities.

The *Wind Turbine Optical Images dataset* consists of 431 images, covering various types of surface damages on wind turbine blades, such as erosion, cracks, oil leakage, and damaged lightning receptors.

The *Solar Panel Optical Images (Small)* dataset contains 516 images, focusing on the effects of soiling on power production for control PV panels.

The *Solar Panel Optical Images (Large)* dataset includes 122 high-resolution long shots of PV panels covered by dust.

The *Solar Panel Infrared Images* dataset comprises 67 grayscale images acquired using a Zenmuse XT IR camera with a DJI Matrice 100 drone, annotated for snail trails and hot spot failures.

| Image set                          | Image type | Captured object | Acquisition by | Resolution               | Color | N   | Ref.                                                                                                 |
| ---------------------------------- | ---------- | --------------- | -------------- | ------------------------ | ----- | --- | ---------------------------------------------------------------------------------------------------- |
| Wind turbine optical images        | Optical    | Wind turbine    | Drone          | 100 × 100–1844 × 1281 | Yes   | 431 | [Shihavuddin et al. (2019)](https://www.sciencedirect.com/science/article/pii/S2352484721005102#bib1)   |
| Solar panel optical images (small) | Optical    | PV panel        | Drone          | 192 × 192               | Yes   | 516 | [Mehta et al. (2018)](https://www.sciencedirect.com/science/article/pii/S2352484721005102#bib1).        |
| Solar panel optical images (large) | Optical    | PV panel        | Drone          | 3264 × 1836             | Yes   | 122 | Original data                                                                                        |
| Solar panel infrared images        | Infrared   | PV panel        | Handhold       | 336 × 256               | No    | 67  | [Alfaro-Mejía et al. (2019)](https://www.sciencedirect.com/science/article/pii/S2352484721005102#bib1) |

The dataset is a valuable resource for studying and developing damage detection models across different power plant types and image modalities.
