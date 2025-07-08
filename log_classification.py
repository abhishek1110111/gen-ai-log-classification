from regex_processor import classification_with_regex
from Bert_processor import classification_with_bert
from llm_processor import classification_with_llm


def classify(logs):
    ''' Classify the given logs using the given classification function.'''
    labels = []
    for source, log_msg in logs:
        label = classify_log(source, log_msg)
        labels.append(label)
    return labels


def classify_log(source, log_msg):
    ''' Classify the given log message using the given classification function.'''
    if source == "LegacyCRM":
        label = classification_with_llm(log_msg)
    else:
        label = classification_with_regex(log_msg)
        if not label:
            label = classification_with_bert(log_msg)
    return label

def classify_csv(input_file):
    ''' Classify the given CSV file using the given classification function.'''
    import pandas as pd
    df = pd.read_csv(input_file)
    # Perform classification
    df["target_label"] = classify(list(zip(df["source"], df["log_message"])))

    # Save the modified file
    output_file = "resources/output.csv"
    df.to_csv(output_file, index=False)

    return output_file

if __name__ == '__main__':
    classify_csv("resources/test.csv")


