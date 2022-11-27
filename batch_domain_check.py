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

def optimize_csv(univ_csv, auth_csv, output):
    """
    add features: univeristy name, sorting by authentication levels
    """
    univ_df = pd.read_csv(univ_csv)
    auth_df = pd.read_csv(auth_csv)
    result_df = univ_df.join(auth_df, lsuffix="_other")[["name", "domain", "SPF", "DMARC", "DKIM"]]
    result_df.to_csv(output)

if __name__ == "__main__":
    # input = "test.csv"
    # output = "test_out.csv"
    univ_csv = "domainList.csv"
    auth_csv = "Chinese_college_authentication.csv"
    output = "new_college_auth.csv"
    optimize_csv(univ_csv, auth_csv, output)
    
    

