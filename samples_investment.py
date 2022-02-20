import semantic_signatures as ss
from buildtrsx.build_samples.build_utterances import generate_utterances

# MAKE_INVESTMENT
sem_sig = [
    ss.SS1_S1,
    ss.SS1_S2,
    ss.SS1_S3,
    ss.SS1_S4,
    ss.SS1_S5,
    ss.SS1_S6,
    ss.SS1_S7,
    ss.SS2_S1,
    ss.SS3_S1,
    ss.SS3_S2,
    ss.SS4_S1,
]
utterances = []
for sig in sem_sig:
    utterances += generate_utterances(sig)

print(len(utterances))

with open("data_augmentation/make_investment.txt", "w", encoding="utf-8") as f:
    for utterance in utterances:
        f.write(utterance)
        f.write("\n")
