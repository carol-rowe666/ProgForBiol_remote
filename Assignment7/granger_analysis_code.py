"""Analysis code for Dr. Granger's project"""
import urllib
import csv

def get_gc_content(seq):
    """Determine the GC content of a sequence"""
    gc_content = 100.0 * (seq.count('G') + seq.count('C')) / len(seq)
    return gc_content

def get_size_class(earlength):
    """Determine the size class of earlength based on Dr. Grangers specification"""
    earlength = float(earlength)
    if earlength > 15.0:
        size_class = 'extralarge'
    elif earlength > 10.0:
        size_class = 'large'
    elif earlength > 8.0:
        size_class = 'medium'
    else:
        size_class = 'small'
    return size_class

def get_data_from_web(url, datatype, headerrow=True):
    """Retrieve CSV data from the web and store it in a list of lists"""
    webpage = urllib.urlopen(url)
    datareader = csv.reader(webpage)
    if headerrow == True:
        datareader.next()
    data = []
    for row in datareader:
        data.append(row)
    return data

def export_to_csv(data, filename):
    """Export a list of lists to a CSV file"""
    output_file = open(filename, 'w')
    datawriter = csv.writer(output_file)
    datawriter.writerows(data)
    output_file.close()

if __name__ == '__main__':
    elves_data = get_data_from_web('http://www.programmingforbiologists.org/data/houseelf_earlength_dna_data.csv', 'str')
    
    #Determine individual level earth length category and gc content values
    results = []
    for indiv_id, earlength, dna in elves_data:
        gc_content = get_gc_content(dna)
        earlength_size_class = get_size_class(earlength)
        indiv_result = [indiv_id, earlength_size_class, gc_content]
        results.append(indiv_result)

    #Get average values of gc content for each size class
    transposed_results = zip(*results)
    sizes = transposed_results[1]
    size_classes = set(sizes)
    gc_content = transposed_results[2]
    results = []
    for size_class in size_classes:
        gc_vals = [gc_content[i] for i in range(len(gc_content)) if sizes[i]==size_class]
        avg_gc_content = sum(gc_vals) / len(gc_vals)
        results.append([size_class, avg_gc_content])
    export_to_csv(results, 'grangers_output.csv')
