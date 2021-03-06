import WORC

# Create network
network = WORC.WORC('example')

# Below are the minimal inputs: you can also use features instead of images and segmentations.
# You need to change these to your sources: check the FASTR documentation.
network.images.append('xnat://xnat.example.nl/search?project=projectid&subjects=subject[0-9][0-9][0-9]&experiments=*_LIVER&scans=T2W&resources=NIFTI&insecure=true')
network.segmentations.append('vfsregex://exmaplemount/somedir/.*.nii')
network.labels.append('vfs://mount/somedir/labels.txt')

# Default classifier is 3rd order polynomial SVM
config = network.defaultconfig()
config['Classification']['classifier'] = 'RF'
network.configs.append(config)

# Build the network: the returned network.network object is a FASTR network.
network.build()

# Convert your appended sources to actual sources in the network.
network.set()

# Execute the network
network.execute()
