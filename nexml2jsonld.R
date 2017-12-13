library(devtools)
load_all('.')
fn <- commandArgs(trailingOnly=TRUE)[1];
ex <- readChar(fn, file.info(fn)$size);
print(xml_to_json(ex));