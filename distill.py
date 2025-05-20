
from model2vec.distill import distill

models = [
    "neuralmind/bert-base-portuguese-cased", # BERTimbau
    "neuralmind/bert-large-portuguese-cased", # BERTimbau
    "pierreguillou/bert-base-cased-squad-v1.1-portuguese",
    "PORTULAN/serafim-100m-portuguese-pt-sentence-encoder",
    "PORTULAN/serafim-335m-portuguese-pt-sentence-encoder",
    #"PORTULAN/serafim-900m-portuguese-pt-sentence-encoder",  # fails
    "PORTULAN/serafim-100m-portuguese-pt-sentence-encoder-ir",
    "PORTULAN/serafim-335m-portuguese-pt-sentence-encoder-ir",
    #"PORTULAN/serafim-900m-portuguese-pt-sentence-encoder-ir", # fails
    #"PORTULAN/albertina-900m-portuguese-ptpt-encoder", # fails
    "PORTULAN/albertina-100m-portuguese-ptpt-encoder",
    #"PORTULAN/albertina-1b5-portuguese-ptpt-encoder", # fails
    #"PORTULAN/albertina-1b5-portuguese-ptpt-encoder-256", # fails
    #"PORTULAN/albertina-900m-portuguese-ptbr-encoder", # fails
    "PORTULAN/albertina-100m-portuguese-ptbr-encoder",
    #"PORTULAN/albertina-900m-portuguese-ptbr-encoder-brwac", # fails
    #"PORTULAN/albertina-1b5-portuguese-ptbr-encoder", # fails
    #"PORTULAN/albertina-1b5-portuguese-ptbr-encoder-256", # fails

    "projecte-aina/roberta-large-ca-v2",
    "projecte-aina/distilroberta-base-ca-v2",
    "projecte-aina/roberta-base-ca-cased-sts",
    "projecte-aina/roberta-base-ca-v2-cased-tc",
    "projecte-aina/roberta-base-ca-v2-massive",
    "projecte-aina/roberta-base-ca-v2-cawikitc",
    "projecte-aina/roberta-base-ca-v2-cased-qa",
    "projecte-aina/roberta-large-ca-v2-massive",
    "projecte-aina/roberta-large-ca-paraphrase",
    #"BSC-LT/mRoBERTa",  # fails
    #"BSC-LT/RoBERTa-ca",  # fails

    "dvilares/bertinho-gl-small-cased",
    "dvilares/bertinho-gl-base-cased",

    "google-bert/bert-base-multilingual-cased",
    "sentence-transformers/LaBSE",
    "sentence-transformers/paraphrase-multilingual-mpnet-base-v2",
    "sentence-transformers/distiluse-base-multilingual-cased-v2",
    "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2",
]

for m in models:
    print(m)
    m2v_model = distill(model_name=m, pca_dims=256)
    m2v_model.save_pretrained(m + "-distill256")


