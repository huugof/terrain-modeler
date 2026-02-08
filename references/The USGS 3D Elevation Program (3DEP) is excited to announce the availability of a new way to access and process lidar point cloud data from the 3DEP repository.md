

3DEP has been acquiring three-dimensional information across the United States using light detection and ranging (lidar) technology- an airborne laser-based remote sensing technology that collects billions of lidar returns while flying- and making results available to the public. The USGS has been strategically focused on providing new mechanisms to access 3DEP data beyond simple downloads. With 3DEP’s adoption of cloud storage and computing, users now have the option to work with massive lidar point cloud datasets without having to download them to local machines.

Recently, USGS began uploading 3DEP lidar point cloud data into an Amazon s3://usgs-lidar Requester Pays bucket*. Currently there are over 1.77 million ASPRS LAS tiles compressed using the LASzip compression encoding in the us-west-2 region, which equates to over 12 trillion lidar point cloud records available from over 1,254 projects across the United States. This resource provides users a mechanism to retrieve and work with 3DEP data that is quicker than the free FTP download protocol.

“The 3D Elevation Program was founded on the concept that high-resolution elevation data should be provided unlicensed, free and open to the public,” explained Kevin Gallagher, Associate Director for USGS Core Science System. “This agreement with Amazon helps to fulfill that promise by providing cloud-access to the trillions of data points collected through the Program.  The democratization of elevation data is a tremendous achievement by the community of partners leading this effort and promises to revolutionize approaches to applications from flood forecasting and geologic assessments to precision agriculture and infrastructure development.”

Hobu, Inc. and the U.S Army Corps of Engineers (USACE) Cold Regions Research and Engineering Laboratory (CRREL) collaborated with the Amazon Web Services (AWS) Public Datasets team to organize these data as Entwine Point Tile (EPT) resources, which is a lossless, streamable octree based on LASzip (LAZ) encoding. The data are now part of the Open Data registry provided by AWS*, similar to the Landsat archive. You can find out more about this project on the AWS Public Dataset page.  https://registry.opendata.aws/usgs-lidar/
Media
View of the WebGL visualization page, https://usgs.entwine.io/
Sources/Usage: Public Domain. View Media Details
View of the WebGL visualization page, https://usgs.entwine.io/.&nbsp; (Public domain.)

“The ability to use cloud computing with free, open 3DEP data will foster amazing new applications and uses of these data that we could not have done before,“ said Jason Stoker, Chief Elevation Scientist for the USGS National Geospatial Program. “Just being able to see an entire statewide project with hundreds of billions of points at one time from a browser is amazing, let alone the potential to process and analyze all these data together in new and innovative ways. We greatly appreciate AWS making a copy of our data available as a Public Dataset, and kudos to Hobu Inc. and USACE CRREL for processing and organizing these data in a way that enables access in an open source fashion.  I can’t wait to see how people take advantage of this effort.”

We would love to hear from anyone who uses this new Public Dataset option. Please provide feedback at 3dep@usgs.gov.

For more information on the 3DEP Program and USGS Elevation Data go to: https://usgs.gov/3DEP

* USGS Product Names Disclaimer: Any use of trade, firm, or product names is for descriptive purposes only and does not imply endorsement by the U.S. Government.
Media
Pre-Hurricane Maria lidar point cloud
Sources/Usage: Public Domain. View Media Details
Figure 1: An example of viewing the entire Pre-Hurricane Maria lidar point cloud dataset collected over Puerto Rico in a web browser. Over 116 billion lidar returns were collected for this project. Points colored by laser intensity (blue = low intensity, red = high intensity).  (Public domain.)
Media
Lidar point cloud, zoom in
Sources/Usage: Public Domain. View Media Details
Figure 2: Zooming in to red rectangle A from figure 1. Points colored by laser intensity (blue = low intensity, red = high intensity).(Public domain.)
Media
Lidar point cloud, Pre-Hurricane PR, rotate and zoom
Sources/Usage: Public Domain. View Media Details
Figure 3: Zooming in and rotating scene in 3D from figure 2. Points colored by laser intensity (blue = low intensity, red = high intensity).  (Public domain.)
