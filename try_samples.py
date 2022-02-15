from buildtrsx.build_samples.build_samples import trsx_sample_node, trsx_samples_node

sample_atr = {"intentref": "MAKE_INVESTMENT", "count": "1", "excluded": "false"}
sample1 = "faire un dépôt de 1500 dollars à mon compte REER"
sample2 = "faire un dépôt de 100 dollars à mon CELI"

print(trsx_sample_node(sample=sample1, sample_atr=sample_atr))
print(trsx_samples_node(samples={sample1: sample_atr, sample2: sample_atr}))

# remark: the annotations will be generated in the data augmentation process
