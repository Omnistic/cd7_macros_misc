clr.AddReferenceByPartialName('Zeiss.Micro.AMP')
from Zeiss.Micro.AMP.Scripting import LiveScanScriptingPlugin

ZenLiveScan = LiveScanScriptingPlugin.Instance
exp = ZenExperiment()

file_prefix = 'multislide-'
exp_prefix = 'exp_slide'
save_folder = 'D:\\UserData\\Transfer\\'

exp_suffix_format = '_{:02d}'

containers = ['A1', 'A2', 'A3']

print('=== START MACRO ===')

for ii, container in enumerate(containers):
    print('Moving to container {}.'.format(container))
    ZenLiveScan.MoveToContainer(container)
    
    exp_suffix = exp_suffix_format.format(ii+1)
    exp_name = exp_prefix + exp_suffix
    
    if exp.Load(exp_name+'.czexp'):
        print('Executing experiment {}...'.format(exp_name))
        image = Zen.Acquisition.Execute(exp)
        print('Experiment complete.')
        
        file_path = save_folder + file_prefix + exp_name + '.czi'
        print('Saving as {}...'.format(file_path))
        if image.Save(file_path, 100, ZenSaveCompressionMode.Compressed, ZenCompressionMethod.Zstd):
            image.Close()
            print('Image saved.')
        else:
            print('Error: file {} could not be saved.'.format(file_path))
    else:
        print('Error: experiment file {} not found.'.format(exp_name))

print('=== END MACRO ===')
