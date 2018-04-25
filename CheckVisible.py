# CheckVisible.m

    
@function
def CheckVisible(M=None,P1=None,P2=None,P3=None,*args,**kwargs):
    varargin = CheckVisible.varargin
    nargin = CheckVisible.nargin

    # used to check if the surface normal facing the camera
#  M: 3x4 projection matrix
#  P1, P2, P3: 3D points
    
    tri_normal=cross((P2 - P1),(P3 - P2))
# CheckVisible.m:6
    
    cam_dir=matlabarray(cat([M[3,1]],[M[3,2]],[M[3,3]]))
# CheckVisible.m:8
    
    if (dot(cam_dir,tri_normal) < 0):
        bVisible=1
# CheckVisible.m:11
        #fprintf('Visible!\n');
    else:
        bVisible=0
# CheckVisible.m:14
        #fprintf('inVisible!\n');
    
