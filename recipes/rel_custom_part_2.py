from prodigy.util import get_labels, split_string
from typing import List, Optional, Union, Iterable
import prodigy
from prodigy.recipes.rel import manual as rel_manual


@prodigy.recipe(
    "custom.rel.manual",
    dataset=("Dataset to save annotations to", "positional", None, str),
    spacy_model=("Loadable spaCy model or blank:lang (e.g. blank:en)", "positional", None, str),
    source=("Data to annotate (file path or '-' to read from standard input)", "positional", None, str),
    loader=("Loader (guessed from file extension if not set)", "option", "lo", str),
    label=(
            "Comma-separated relation label(s) to annotate or text file with one label per line", "option", "l",
            get_labels),
    span_label=(
            "Comma-separated span label(s) to annotate or text file with one label per line", "option", "sl",
            get_labels),
    patterns=("Patterns file for defining custom spans to be added", "option", "pt", str),
    disable_patterns=("Patterns file for defining tokens to disable (make unselectable)", "option", "dpt", str),
    add_ents=("Add entities predicted by the model", "flag", "AE", bool),
    add_nps=("Add noun phrases (if noun chunks rules are available), based on tagger and parser", "flag", "AN"),
    wrap=("Wrap lines in the UI by default (instead of showing tokens in one row)", "flag", "W", bool),
    exclude=("Comma-separated list of dataset IDs whose annotations to exclude", "option", "e", split_string),
    hide_arrow_heads=("Hide the arrow heads visually", "option", "HA", bool),
)
def custom_rel_manual(dataset: str,
                      spacy_model: str,
                      source: Union[str, Iterable[dict]] = "-",
                      loader: Optional[str] = None,
                      label: Optional[List[str]] = None,
                      span_label: Optional[List[str]] = None,
                      exclude: Optional[List[str]] = None,
                      patterns: Optional[Union[str, List]] = None,
                      disable_patterns: Optional[Union[str, List]] = None,
                      add_ents: bool = False,
                      add_nps: bool = False,
                      wrap: bool = False,
                      hide_arrow_heads: bool = False):
    components = rel_manual(
        dataset=dataset,
        spacy_model=spacy_model,
        source=source,
        loader=loader,
        label=label,
        span_label=span_label,
        exclude=exclude,
        patterns=patterns,
        disable_patterns=disable_patterns,
        add_ents=add_ents,
        add_nps=add_nps,
        wrap=wrap,
        hide_arrow_heads=hide_arrow_heads, )

   # components["config"]["label_style"] = "dropdown"
    components["config"]["feed_overlap"] = True
    components["config"]["force_stream_order"] = True
    # Add callback to the components returned by the recipe
    components["validate_answer"] = validate_answer
    components["config"]["global_css"] = ".prodigy-button-reject, .prodigy-button-ignore {display: none}"
    components["config"]["custom_theme"]["labels"] = {
        "PK": "#dddddd",
        "VALUE": "#dddddd",
        "UNITS": "#dddddd",
        "TYPE_MEAS": "#dddddd",
        "COMPARE": "#dddddd",
        "RANGE": "#dddddd",
        "CHEMICAL": "#e38305",
        "SPECIES": "#0595e3",
        "CONTEXT": "#17e305",
        "ROUTE": "#e305af",
        "DISEASE": "#e3df05",
        "C_VAL": "#f51307",
        "D_VAL": "#dddddd",
        "RELATED": "#04d438",
        "DOSE": "#04b5d4",
    }
    components["config"]["instructions"] = "./recipes/instructions.html"
    components["config"]["batch_size"] = 5
    components["config"]["history_size"] = 5
    components["config"]["show_flag"] = True
    # ===== Add block for comments ===== #
    blocks = [
        {"view_id": components['view_id']},
        {"view_id": "text_input", "field_rows": 3, "field_label": "Write any comments here"}
    ]
    components['view_id'] = 'blocks'
    components['config']['blocks'] = blocks
    components['stream'] = list(components['stream'])

    return components


def validate_answer(eg):
    error_messages = []
    for relation in eg['relations']:
        head_label = relation['head_span']['label']
        child_label = relation['child_span']['label']
        rel_type = relation['label']
        is_valid = (head_label, child_label) in valid_relations[rel_type]
        if not is_valid:
            error_messages.append(
                "Careful!, you can't assign a relation type" + rel_type + " between:\n" + head_label + "-" +
                child_label)

    if error_messages:
        raise ValueError(error_messages)


valid_relations = {
    "C_VAL": [
        ("PK", "VALUE"), ("PK", "RANGE")
    ],
    "D_VAL": [
        ("VALUE", "VALUE"), ("RANGE", "RANGE"), ("RANGE", "VALUE"), ("VALUE", "RANGE")
    ],
    "RELATED": [
        ("TYPE_MEAS", "VALUE"), ("TYPE_MEAS", "RANGE"),
        ("COMPARE", "VALUE"), ("COMPARE", "RANGE"),
        ("UNITS", "VALUE"), ("UNITS", "RANGE"),

        ("SPECIES", "VALUE"), ("SPECIES", "RANGE"),
        ("CHEMICAL", "VALUE"), ("CHEMICAL", "RANGE"),
        ("DISEASE", "VALUE"), ("DISEASES", "RANGE"),
        ("ROUTE", "VALUE"), ("ROUTE", "RANGE"),
        ("CONTEXT", "VALUE"), ("CONTEXT", "RANGE")
    ],

    "DOSE": [("VALUE", "VALUE"), ("RANGE", "RANGE"), ("RANGE", "VALUE"), ("VALUE", "RANGE")]

}