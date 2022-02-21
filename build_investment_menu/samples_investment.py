import semantic_signatures as ss
import semantic_signatures_fr as ssf
from buildtrsx.build_samples.build_utterances import generate_utterances


def save_utterances(sim_sigs: list, n: int, file_name: str):
    utterances = []
    for sig in sim_sigs:
        utterances += generate_utterances(sig, sample_size=n)

    with open("data_augmentation/" + file_name + ".txt", "w", encoding="utf-8") as f:
        for utterance in utterances:
            f.write(utterance)
            f.write("\n")


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

sem_sig_f = [
    ssf.SS1_S1,
    ssf.SS1_S2,
    ssf.SS1_S3,
    ssf.SS2_S1,
    ssf.SS2_S2,
    ssf.SS3_S1,
    ssf.SS3_S2,
    ssf.SS3_S3,
    ssf.SS3_S4,
    ssf.SS4_S1,
    ssf.SS4_S2,
    ssf.SS4_S3,
]

save_utterances(sem_sig, 20, "make_investment")
save_utterances(sem_sig_f, 20, "make_investment_fr")
