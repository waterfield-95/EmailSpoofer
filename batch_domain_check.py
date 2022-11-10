from check_domain_dds import check_dds
import pandas as pd

def batch_processing(input_file, output_file):
    # file.txt consists of multiple domains, each on one line
    d = {
        "domain": [],
        "SPF": [],
        "DKIM": [],
        "DMARC": [],
    }
    with open(input_file) as f:
        for line in f:
            # result: [spf, dkim, dmarc]
            #todo: for one line, check all domain for the college in one row
            domain = line.split(" ")[0].strip()
            print(domain)
            result = check_dds(domain)
            d["domain"].append(domain)
            d["SPF"].append(result[0])
            d["DKIM"].append(result[1])
            d["DMARC"].append(result[2])
    
    df = pd.DataFrame(d)
    df.to_csv(output_file)
    print(pd.read_csv(output_file))
    
if __name__ == "__main__":
    # input = "test.txt"
    # output = "test.csv"
    input = "Chinese_college_domains.txt"
    output = "Chinese_college_authentication.csv"
    batch_processing(input, output)
            

