<!-- SPACY PROJECT: AUTO-GENERATED DOCS START (do not remove) -->

# 💊 UNODC Project: Detecting Drug Seizure Information in Open Source News Articles (Named Entity Recognition)

This project uses streaming news data from [`JRC XML Newsfeeds`](https://medisys.newsbrief.eu/rss/?type=category&id=heroinseizure&language=all&duplicates=false) and [GDELT News API](https://blog.gdeltproject.org/gdelt-geo-2-0-api-debuts/) to bootstrap an NER model to detect drug seizures in news articles. As an additional source for model training, this project uses [Reddit comments](https://files.pushshift.io/reddit/comments/) for both informal example of drug usage ("hits of acid") or for false positive examples ("I used 1 gr of heroin last week"). 

| [`JRC Example`](https://medisys.newsbrief.eu/rss/?type=category&id=heroinseizure&language=all&duplicates=false) 
| [`GDELT Example`](https://api.gdeltproject.org/api/v2/doc/doc?query=heroin&contentmode=ArtList&maxrecords=250&format=json&timespan=1d) |
[`NewsAPI Example`](https://medisys.newsbrief.eu/rss/?type=category&id=heroinseizure&language=all&duplicates=false) |

## 📋 project.yml

The [`project.yml`](project.yml) defines the data assets required by the
project, as well as the available commands and workflows. For details, see the
[spaCy projects documentation](https://spacy.io/usage/projects).

### ⏯ Commands

The following commands are defined by the project. They
can be executed using [`spacy project run [name]`](https://spacy.io/api/cli#project-run).
Commands are only re-run if their inputs have changed.

| Command | Description |
| --- | --- |
| `preprocess` | Convert the data to spaCy's binary format |
| `train` | Train a named entity recognition model |
| `evaluate` | Evaluate the model and export metrics |
| `package` | Package the trained model so it can be installed |
| `visualize-model` | Visualize the model's output interactively using Streamlit |
| `visualize-data` | Explore the annotated data in an interactive Streamlit app |

### ⏭ Workflows

The following workflows are defined by the project. They
can be executed using [`spacy project run [name]`](https://spacy.io/api/cli#project-run)
and will run the specified commands in order. Commands are only re-run if their
inputs have changed.

| Workflow | Steps |
| --- | --- |
| `all` | `preprocess` &rarr; `train` &rarr; `evaluate` |

### 🗂 Assets

The following assets are defined by the project. They can
be fetched by running [`spacy project assets`](https://spacy.io/api/cli#project-assets)
in the project directory.

| File | Source | Description |
| --- | --- | --- |
| [`assets/drug_seizures_training.jsonl`](assets/drug_seizures_training.jsonl) | Local | JSONL-formatted training data exported from Prodigy, annotated with `DRUG_SEIZURE` entities (1654 examples) |
| [`assets/drug_seizures_eval.jsonl`](assets/drug_seizures_eval.jsonl) | Local | JSONL-formatted development data exported from Prodigy, annotated with `DRUG_SEIZURE` entities (535 examples) |
| [`assets/patterns`](assets/patterns) | Local | Patterns file generated to pre-highlight during annotation (7 pattern files) |

### 🔧 Maintenance
#### Adding new data
**** 
Add a thorough description here to help REPRODUCE the injection and updating of new training examples. The data will need to be preprocessed using the preprocess command. The data will also need to be split into proportions for training and eval data sets. A condensed input example is below.
```
{"text":"ANF Rawalpindi arrested Afghan Citizen Muhammad Naveed from Islamabad International Airport and recovered 798 Grams Amphetamine from his personal possession.","_input_hash":932777898,"_task_hash":-313169072,"tokens":[{"text":"ANF","start":0,"end":3,"id":0,"ws":true},{"text":"Rawalpindi","start":4,"end":14,"id":1,"ws":true},{"text":"arrested","start":15,"end":23,"id":2,"ws":true},{"text":"Afghan","start":24,"end":30,"id":3,"ws":true},{"text":"Citizen","start":31,"end":38,"id":4,"ws":true},{"text":"Muhammad","start":39,"end":47,"id":5,"ws":true},{"text":"Naveed","start":48,"end":54,"id":6,"ws":true},{"text":"from","start":55,"end":59,"id":7,"ws":true},{"text":"Islamabad","start":60,"end":69,"id":8,"ws":true},{"text":"International","start":70,"end":83,"id":9,"ws":true},{"text":"Airport","start":84,"end":91,"id":10,"ws":true},{"text":"and","start":92,"end":95,"id":11,"ws":true},{"text":"recovered","start":96,"end":105,"id":12,"ws":true},{"text":"798","start":106,"end":109,"id":13,"ws":true},{"text":"Grams","start":110,"end":115,"id":14,"ws":true},{"text":"Amphetamine","start":116,"end":127,"id":15,"ws":true},{"text":"from","start":128,"end":132,"id":16,"ws":true},{"text":"his","start":133,"end":136,"id":17,"ws":true},{"text":"personal","start":137,"end":145,"id":18,"ws":true},{"text":"possession","start":146,"end":156,"id":19,"ws":false},{"text":".","start":156,"end":157,"id":20,"ws":true}],"spans":[{"text":"798 Grams","source":"en_core_web_lg","input_hash":932777898,"start":106,"end":115,"token_start":13,"token_end":14,"label":"QUANTITY"},{"start":116,"end":127,"token_start":15,"token_end":15,"label":"DRUG"}],"_session_id":null,"_view_id":"ner_manual","answer":"accept"}
``` 
#### Updating the model

To update the models with new training data or to simply test new configurations, one can re-run the `train` workflow on the new data. Only outputs which outperform the F1-scores in the previous models will be saved to the [`model-best`](training/model-best) file location. 

#### Adding new labels

It is not recommended to add new labels to this current model as the additional labeled entities can create accuracy problems from [`weak supervision`](https://en.wikipedia.org/wiki/Weak_supervision) or [`label noise`](https://arxiv.org/abs/2003.10471). If there is a need to create a new NER model with different labels in the future, it is recommended to create a separate model altogether. However, if one is determined to add additional labels to this model, then one must FIRST re-annotate all of the training and eval data in this package before introducing new training examples as there may be the possibility that entities already existed in the corpus that was not labeled.



<!-- SPACY PROJECT: AUTO-GENERATED DOCS END (do not remove) -->

---

## 💉 Drug Data



| Entity Labels | Examples | Description |
| --- | --- | --- |
| DRUG | Heroin, crack, weed | Illicit drugs or presursor substances identified by the UNODC |
| GPE | Hong Kong, Vienna | Geopolitical entity, i.e. countries, cities, states |
| QUANTITY | 10 gr, ten grams, forty-five 'hits' | Numerical value or numerical 'likeness' (e.g. 100 or one-hundred) followed immediately by a weight classification unit (Kg, grams, tonnes) |
| ORG | Drug Enforcement Agency, HK Customs, RCMP | The name of the agency responsible for the illicit drug seizure |
| FACILITY | Washington Monument, Toronto Pearson Airport | Washington Monument, Toronto Pearson Airport |
|*Note that UNODC refers to this entity as "Installation" |
| CONCEAL | Suitcase, Front Bumper, Body Cavity | Specific location where person(s) attempted to place an illicit drug quantity out of sight from authorities |

The file for the NER labels is here: [`assets/labels/ner.json`](assets/labels/ner.json)

Below is are some jsonl formatted pattern examples available here: [`assets/patterns`](assets/patterns) which are useful for a rule-based entity extraction approach. 
```
{"label": "GPE", "pattern": [{"lower": "republic"}, {"lower": "of"}, {"lower": "armenia"}]}
{"label":"CONCEAL","pattern":[{"lower":"bottles"},{"lower":"of"},{"lower":"vitamin"},{"lower":"c"}]}
{"label":"DRUG","pattern":[{"lower":"black"}, {"lower":"tar"}, {"lower":"heroin"}]}
```


| File                                                                    | Count | Description                                                                                                                                                                                                                                                                                                                                                                                    |
| ----------------------------------------------------------------------- | ----: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [`assets/patterns`](assets/drug_seizures_training.jsonl) |   7 (files) | Match patterns used to bootstrap the annotation process.|
| [`assets/drug_seizures_training.jsonl`](assets/drug_seizures_training.jsonl) |  1654 | Training data for `DRUG_SEIZURE` entities. |
| [`assets/drug_seizures_training.jsonl`](assets/drug_seizures_training.jsonl)         |   535 | Evaluation data for Training data for `DRUG_SEIZURE` entities. |

<img width="250" src="/home/esteban/dmp_ner_3.0/visualize_model.png" alt="" align="right">

### Visualize the data and model

The [`visualize_data.py`](scripts/visualize_data.py) script lets you visualize
the training and evaluation datasets with
[displaCy](https://spacy.io/usage/visualizers).

```bash
python -m spacy project run visualize-data
```

The [`visualize_model.py`](scripts/visualize_model.py) script is powered by
[`spacy-streamlit`](https://github.com/explosion/spacy-streamlit) and lets you
explore the trained model interactively.

```bash
python -m spacy project run visualize-model
```

### Training and evaluation data format

The training and evaluation datasets are distributed in Prodigy's simple JSONL
(newline-delimited JSON) format. Each entry contains a `"text"` and a list of
`"spans"` with the `"start"` and `"end"` character offsets and the `"ents"` of
the annotated entities. The data also includes the tokenization. Here's a
simplified example entry:

```json
{"text": "The Quảng Ngãi Province Police Department seized 100 kilos of cocaine hidden inside a Toyota rear trunk outside of Quảng Ngãi at the railroad station.",
  "ents": [
    {"start": 4, "end": 41, "label": "ORG"},
    {"start": 49, "end": 58, "label": "QUANTITY"},
    {"start": 62, "end": 69, "label": "DRUG"},
    {"start": 86, "end": 103, "label": "CONCEAL"},
    {"start": 115, "end": 125, "label": "GPE"},
    {"start": 133, "end": 149, "label": "FAC"
    }
  ]
}
```