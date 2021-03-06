import mxnet as mx

def get_sym():
    '''
    image:(1,3,368,368)
    center_map:(1,1,368,368)

    '''
    image = mx.symbol.Variable(name='image')
    center_map = mx.symbol.Variable(name='center_map')
    pool_center_lower = mx.symbol.Pooling(name='pool_center_lower', data=center_map , pooling_convention='full', pad=(0,0), kernel=(9,9), stride=(8,8), pool_type='avg')
    conv1_stage1 = mx.symbol.Convolution(name='conv1_stage1', data=image , num_filter=128, pad=(4,4), kernel=(9,9), stride=(1,1), no_bias=False,workspace=2048)
    relu1_stage1 = mx.symbol.Activation(name='relu1_stage1', data=conv1_stage1 , act_type='relu')
    pool1_stage1 = mx.symbol.Pooling(name='pool1_stage1', data=relu1_stage1 , pooling_convention='full', pad=(0,0), kernel=(3,3), stride=(2,2), pool_type='max')
    conv2_stage1 = mx.symbol.Convolution(name='conv2_stage1', data=pool1_stage1 , num_filter=128, pad=(4,4), kernel=(9,9), stride=(1,1), no_bias=False,workspace=2048)
    relu2_stage1 = mx.symbol.Activation(name='relu2_stage1', data=conv2_stage1 , act_type='relu')
    pool2_stage1 = mx.symbol.Pooling(name='pool2_stage1', data=relu2_stage1 , pooling_convention='full', pad=(0,0), kernel=(3,3), stride=(2,2), pool_type='max')
    conv3_stage1 = mx.symbol.Convolution(name='conv3_stage1', data=pool2_stage1 , num_filter=128, pad=(4,4), kernel=(9,9), stride=(1,1), no_bias=False,workspace=2048)
    relu3_stage1 = mx.symbol.Activation(name='relu3_stage1', data=conv3_stage1 , act_type='relu')
    pool3_stage1 = mx.symbol.Pooling(name='pool3_stage1', data=relu3_stage1 , pooling_convention='full', pad=(0,0), kernel=(3,3), stride=(2,2), pool_type='max')
    conv4_stage1 = mx.symbol.Convolution(name='conv4_stage1', data=pool3_stage1 , num_filter=32, pad=(2,2), kernel=(5,5), stride=(1,1), no_bias=False,workspace=2048)
    relu4_stage1 = mx.symbol.Activation(name='relu4_stage1', data=conv4_stage1 , act_type='relu')
    conv5_stage1 = mx.symbol.Convolution(name='conv5_stage1', data=relu4_stage1 , num_filter=512, pad=(4,4), kernel=(9,9), stride=(1,1), no_bias=False,workspace=2048)
    relu5_stage1 = mx.symbol.Activation(name='relu5_stage1', data=conv5_stage1 , act_type='relu')
    conv6_stage1 = mx.symbol.Convolution(name='conv6_stage1', data=relu5_stage1 , num_filter=512, pad=(0,0), kernel=(1,1), stride=(1,1), no_bias=False,workspace=2048)
    relu6_stage1 = mx.symbol.Activation(name='relu6_stage1', data=conv6_stage1 , act_type='relu')
    conv7_stage1 = mx.symbol.Convolution(name='conv7_stage1', data=relu6_stage1 , num_filter=15, pad=(0,0), kernel=(1,1), stride=(1,1), no_bias=False,workspace=2048)
    conv1_stage2 = mx.symbol.Convolution(name='conv1_stage2', data=image , num_filter=128, pad=(4,4), kernel=(9,9), stride=(1,1), no_bias=False,workspace=2048)
    relu1_stage2 = mx.symbol.Activation(name='relu1_stage2', data=conv1_stage2 , act_type='relu')
    pool1_stage2 = mx.symbol.Pooling(name='pool1_stage2', data=relu1_stage2 , pooling_convention='full', pad=(0,0), kernel=(3,3), stride=(2,2), pool_type='max')
    conv2_stage2 = mx.symbol.Convolution(name='conv2_stage2', data=pool1_stage2 , num_filter=128, pad=(4,4), kernel=(9,9), stride=(1,1), no_bias=False,workspace=2048)
    relu2_stage2 = mx.symbol.Activation(name='relu2_stage2', data=conv2_stage2 , act_type='relu')
    pool2_stage2 = mx.symbol.Pooling(name='pool2_stage2', data=relu2_stage2 , pooling_convention='full', pad=(0,0), kernel=(3,3), stride=(2,2), pool_type='max')
    conv3_stage2 = mx.symbol.Convolution(name='conv3_stage2', data=pool2_stage2 , num_filter=128, pad=(4,4), kernel=(9,9), stride=(1,1), no_bias=False,workspace=2048)
    relu3_stage2 = mx.symbol.Activation(name='relu3_stage2', data=conv3_stage2 , act_type='relu')
    pool3_stage2 = mx.symbol.Pooling(name='pool3_stage2', data=relu3_stage2 , pooling_convention='full', pad=(0,0), kernel=(3,3), stride=(2,2), pool_type='max')
    conv4_stage2 = mx.symbol.Convolution(name='conv4_stage2', data=pool3_stage2 , num_filter=32, pad=(2,2), kernel=(5,5), stride=(1,1), no_bias=False,workspace=2048)
    relu4_stage2 = mx.symbol.Activation(name='relu4_stage2', data=conv4_stage2 , act_type='relu')
    concat_stage2 = mx.symbol.Concat(name='concat_stage2', *[relu4_stage2,conv7_stage1,pool_center_lower] )
    Mconv1_stage2 = mx.symbol.Convolution(name='Mconv1_stage2', data=concat_stage2 , num_filter=128, pad=(5,5), kernel=(11,11), stride=(1,1), no_bias=False,workspace=2048)
    Mrelu1_stage2 = mx.symbol.Activation(name='Mrelu1_stage2', data=Mconv1_stage2 , act_type='relu')
    Mconv2_stage2 = mx.symbol.Convolution(name='Mconv2_stage2', data=Mrelu1_stage2 , num_filter=128, pad=(5,5), kernel=(11,11), stride=(1,1), no_bias=False,workspace=2048)
    Mrelu2_stage2 = mx.symbol.Activation(name='Mrelu2_stage2', data=Mconv2_stage2 , act_type='relu')
    Mconv3_stage2 = mx.symbol.Convolution(name='Mconv3_stage2', data=Mrelu2_stage2 , num_filter=128, pad=(5,5), kernel=(11,11), stride=(1,1), no_bias=False,workspace=2048)
    Mrelu3_stage2 = mx.symbol.Activation(name='Mrelu3_stage2', data=Mconv3_stage2 , act_type='relu')
    Mconv4_stage2 = mx.symbol.Convolution(name='Mconv4_stage2', data=Mrelu3_stage2 , num_filter=128, pad=(0,0), kernel=(1,1), stride=(1,1), no_bias=False,workspace=2048)
    Mrelu4_stage2 = mx.symbol.Activation(name='Mrelu4_stage2', data=Mconv4_stage2 , act_type='relu')
    Mconv5_stage2 = mx.symbol.Convolution(name='Mconv5_stage2', data=Mrelu4_stage2 , num_filter=15, pad=(0,0), kernel=(1,1), stride=(1,1), no_bias=False,workspace=2048)
    conv1_stage3 = mx.symbol.Convolution(name='conv1_stage3', data=pool3_stage2 , num_filter=32, pad=(2,2), kernel=(5,5), stride=(1,1), no_bias=False,workspace=2048)
    relu1_stage3 = mx.symbol.Activation(name='relu1_stage3', data=conv1_stage3 , act_type='relu')
    concat_stage3 = mx.symbol.Concat(name='concat_stage3', *[relu1_stage3,Mconv5_stage2,pool_center_lower] )
    Mconv1_stage3 = mx.symbol.Convolution(name='Mconv1_stage3', data=concat_stage3 , num_filter=128, pad=(5,5), kernel=(11,11), stride=(1,1), no_bias=False,workspace=2048)
    Mrelu1_stage3 = mx.symbol.Activation(name='Mrelu1_stage3', data=Mconv1_stage3 , act_type='relu')
    Mconv2_stage3 = mx.symbol.Convolution(name='Mconv2_stage3', data=Mrelu1_stage3 , num_filter=128, pad=(5,5), kernel=(11,11), stride=(1,1), no_bias=False,workspace=2048)
    Mrelu2_stage3 = mx.symbol.Activation(name='Mrelu2_stage3', data=Mconv2_stage3 , act_type='relu')
    Mconv3_stage3 = mx.symbol.Convolution(name='Mconv3_stage3', data=Mrelu2_stage3 , num_filter=128, pad=(5,5), kernel=(11,11), stride=(1,1), no_bias=False,workspace=2048)
    Mrelu3_stage3 = mx.symbol.Activation(name='Mrelu3_stage3', data=Mconv3_stage3 , act_type='relu')
    Mconv4_stage3 = mx.symbol.Convolution(name='Mconv4_stage3', data=Mrelu3_stage3 , num_filter=128, pad=(0,0), kernel=(1,1), stride=(1,1), no_bias=False,workspace=2048)
    Mrelu4_stage3 = mx.symbol.Activation(name='Mrelu4_stage3', data=Mconv4_stage3 , act_type='relu')
    Mconv5_stage3 = mx.symbol.Convolution(name='Mconv5_stage3', data=Mrelu4_stage3 , num_filter=15, pad=(0,0), kernel=(1,1), stride=(1,1), no_bias=False,workspace=2048)
    conv1_stage4 = mx.symbol.Convolution(name='conv1_stage4', data=pool3_stage2 , num_filter=32, pad=(2,2), kernel=(5,5), stride=(1,1), no_bias=False,workspace=2048)
    relu1_stage4 = mx.symbol.Activation(name='relu1_stage4', data=conv1_stage4 , act_type='relu')
    concat_stage4 = mx.symbol.Concat(name='concat_stage4', *[relu1_stage4,Mconv5_stage3,pool_center_lower] )
    Mconv1_stage4 = mx.symbol.Convolution(name='Mconv1_stage4', data=concat_stage4 , num_filter=128, pad=(5,5), kernel=(11,11), stride=(1,1), no_bias=False,workspace=2048)
    Mrelu1_stage4 = mx.symbol.Activation(name='Mrelu1_stage4', data=Mconv1_stage4 , act_type='relu')
    Mconv2_stage4 = mx.symbol.Convolution(name='Mconv2_stage4', data=Mrelu1_stage4 , num_filter=128, pad=(5,5), kernel=(11,11), stride=(1,1), no_bias=False,workspace=2048)
    Mrelu2_stage4 = mx.symbol.Activation(name='Mrelu2_stage4', data=Mconv2_stage4 , act_type='relu')
    Mconv3_stage4 = mx.symbol.Convolution(name='Mconv3_stage4', data=Mrelu2_stage4 , num_filter=128, pad=(5,5), kernel=(11,11), stride=(1,1), no_bias=False,workspace=2048)
    Mrelu3_stage4 = mx.symbol.Activation(name='Mrelu3_stage4', data=Mconv3_stage4 , act_type='relu')
    Mconv4_stage4 = mx.symbol.Convolution(name='Mconv4_stage4', data=Mrelu3_stage4 , num_filter=128, pad=(0,0), kernel=(1,1), stride=(1,1), no_bias=False,workspace=2048)
    Mrelu4_stage4 = mx.symbol.Activation(name='Mrelu4_stage4', data=Mconv4_stage4 , act_type='relu')
    Mconv5_stage4 = mx.symbol.Convolution(name='Mconv5_stage4', data=Mrelu4_stage4 , num_filter=15, pad=(0,0), kernel=(1,1), stride=(1,1), no_bias=False,workspace=2048)
    conv1_stage5 = mx.symbol.Convolution(name='conv1_stage5', data=pool3_stage2 , num_filter=32, pad=(2,2), kernel=(5,5), stride=(1,1), no_bias=False,workspace=2048)
    relu1_stage5 = mx.symbol.Activation(name='relu1_stage5', data=conv1_stage5 , act_type='relu')
    concat_stage5 = mx.symbol.Concat(name='concat_stage5', *[relu1_stage5,Mconv5_stage4,pool_center_lower] )
    Mconv1_stage5 = mx.symbol.Convolution(name='Mconv1_stage5', data=concat_stage5 , num_filter=128, pad=(5,5), kernel=(11,11), stride=(1,1), no_bias=False,workspace=2048)
    Mrelu1_stage5 = mx.symbol.Activation(name='Mrelu1_stage5', data=Mconv1_stage5 , act_type='relu')
    Mconv2_stage5 = mx.symbol.Convolution(name='Mconv2_stage5', data=Mrelu1_stage5 , num_filter=128, pad=(5,5), kernel=(11,11), stride=(1,1), no_bias=False,workspace=2048)
    Mrelu2_stage5 = mx.symbol.Activation(name='Mrelu2_stage5', data=Mconv2_stage5 , act_type='relu')
    Mconv3_stage5 = mx.symbol.Convolution(name='Mconv3_stage5', data=Mrelu2_stage5 , num_filter=128, pad=(5,5), kernel=(11,11), stride=(1,1), no_bias=False,workspace=2048)
    Mrelu3_stage5 = mx.symbol.Activation(name='Mrelu3_stage5', data=Mconv3_stage5 , act_type='relu')
    Mconv4_stage5 = mx.symbol.Convolution(name='Mconv4_stage5', data=Mrelu3_stage5 , num_filter=128, pad=(0,0), kernel=(1,1), stride=(1,1), no_bias=False,workspace=2048)
    Mrelu4_stage5 = mx.symbol.Activation(name='Mrelu4_stage5', data=Mconv4_stage5 , act_type='relu')
    Mconv5_stage5 = mx.symbol.Convolution(name='Mconv5_stage5', data=Mrelu4_stage5 , num_filter=15, pad=(0,0), kernel=(1,1), stride=(1,1), no_bias=False,workspace=2048)
    conv1_stage6 = mx.symbol.Convolution(name='conv1_stage6', data=pool3_stage2 , num_filter=32, pad=(2,2), kernel=(5,5), stride=(1,1), no_bias=False,workspace=2048)
    relu1_stage6 = mx.symbol.Activation(name='relu1_stage6', data=conv1_stage6 , act_type='relu')
    concat_stage6 = mx.symbol.Concat(name='concat_stage6', *[relu1_stage6,Mconv5_stage5,pool_center_lower] )
    Mconv1_stage6 = mx.symbol.Convolution(name='Mconv1_stage6', data=concat_stage6 , num_filter=128, pad=(5,5), kernel=(11,11), stride=(1,1), no_bias=False,workspace=2048)
    Mrelu1_stage6 = mx.symbol.Activation(name='Mrelu1_stage6', data=Mconv1_stage6 , act_type='relu')
    Mconv2_stage6 = mx.symbol.Convolution(name='Mconv2_stage6', data=Mrelu1_stage6 , num_filter=128, pad=(5,5), kernel=(11,11), stride=(1,1), no_bias=False,workspace=2048)
    Mrelu2_stage6 = mx.symbol.Activation(name='Mrelu2_stage6', data=Mconv2_stage6 , act_type='relu')
    Mconv3_stage6 = mx.symbol.Convolution(name='Mconv3_stage6', data=Mrelu2_stage6 , num_filter=128, pad=(5,5), kernel=(11,11), stride=(1,1), no_bias=False,workspace=2048)
    Mrelu3_stage6 = mx.symbol.Activation(name='Mrelu3_stage6', data=Mconv3_stage6 , act_type='relu')
    Mconv4_stage6 = mx.symbol.Convolution(name='Mconv4_stage6', data=Mrelu3_stage6 , num_filter=128, pad=(0,0), kernel=(1,1), stride=(1,1), no_bias=False,workspace=2048)
    Mrelu4_stage6 = mx.symbol.Activation(name='Mrelu4_stage6', data=Mconv4_stage6 , act_type='relu')
    Mconv5_stage6 = mx.symbol.Convolution(name='Mconv5_stage6', data=Mrelu4_stage6 , num_filter=15, pad=(0,0), kernel=(1,1), stride=(1,1), no_bias=False,workspace=2048)

    out=mx.sym.Group([conv7_stage1,Mconv5_stage2,Mconv5_stage3,Mconv5_stage4,Mconv5_stage5,Mconv5_stage6])
    return out

if __name__=='__main__':
    sym=get_sym()
    mx.viz.plot_network(sym, shape={'image': (1, 4, 368, 368),'center_map':(1,1,368,368)}).view()