@mfunction("")
def obj_main(P=None, p_img2=None, M=None, tex_name=None, im_index=None):

    img = imread(tex_name)
    img_size = size(img)

    #----------------------------------------------------
    # mesh-triangulation
    #----------------------------------------------------
    tri = delaunay(p_img2(mslice[:], 1), p_img2(mslice[:], 2))# 2D delaunay

    # trisurf mesh triangulation
    figure(4 + im_index)
    trisurf(tri, P(mslice[:], 1), P(mslice[:], 2), P(mslice[:], 3))

    #----------------------------------------------------
    # output .obj file
    #----------------------------------------------------
    #fid = fopen('model.obj', 'wt');
    cmd_fid = mcat([mstring('fid = fopen(\'model'), num2str(im_index), mstring('.obj\', \'wt\');')])
    eval(cmd_fid)
    fprintf(fid, mstring('# obj file\\n'))
    cmd_print = mcat([mstring('fprintf(fid, \'mtllib model'), num2str(im_index), mstring('.mtl\\n\\n\');')])
    eval(cmd_print)
    fprintf(fid, mstring('usemtl Texture\\n'))

    # output 3D vertex information (3D points)
    [len, dummy] = size(P)
    for i in mslice[1:len]:
        fprintf(fid, mstring('v %f %f %f\\n'), P(i, 1), P(i, 2), P(i, 3))
        end
        fprintf(fid, mstring('\\n\\n\\n'))

        # output vertex texture coordinate (2D points)
        for i in mslice[1:len]:
            # texture mapping
            fprintf(fid, mstring('vt %f %f\\n'), p_img2(i, 1) / img_size(2), 1 - p_img2(i, 2) / img_size(1))
            end
            fprintf(fid, mstring('\\n\\n\\n'))

            # output face information
            [len_tri, dummy] = size(tri)
            bVisible = 0
            for i in mslice[1:len_tri]:
                # 3D mesh normal
                #fprintf('loop %d \n',i);
                bVisible = CheckVisible(M, P(tri(i, 1), mslice[:]).cT, P(tri(i, 2), mslice[:]).cT, P(tri(i, 3), mslice[:]).cT)
                if (bVisible == 1):
                    fprintf(fid, mstring('f %d/%d %d/%d %d/%d\\n'), tri(i, 1), tri(i, 1), tri(i, 2), tri(i, 2), tri(i, 3), tri(i, 3))
                else:
                    fprintf(fid, mstring('f %d/%d %d/%d %d/%d\\n'), tri(i, 2), tri(i, 2), tri(i, 1), tri(i, 1), tri(i, 3), tri(i, 3))
                    end
                    end

                    fclose(fid)

                    #----------------------------------------------------
                    # output .mtl file
                    #----------------------------------------------------
                    cmd_mtl = mcat([mstring('fid_mtl = fopen(\'model'), num2str(im_index), mstring('.mtl\', \'wt\');')])
                    eval(cmd_mtl)
                    fprintf(fid_mtl, mstring('# MTL file\\n'))
                    fprintf(fid_mtl, mstring('newmtl Texture\\n'))
                    fprintf(fid_mtl, mstring('Ka 1 1 1\\nKd 1 1 1\\nKs 1 1 1\\n'))
                    cmd_fprintf = mcat([mstring('fprintf(fid_mtl, \'map_Kd '), tex_name, mstring('\\n\');')])
                    eval(cmd_fprintf)
                    fclose(fid_mtl)