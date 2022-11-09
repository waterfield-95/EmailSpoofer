"""
check if the given domain employed with DMARC, DKIM, SPF authentication protocal
"""

import dns.resolver

def check_DMARC(domain):
    # Testing DMARC
    print()
    print ("Testing domain", domain, "for DMARC record...")
    try:
        test_dmarc = dns.resolver.resolve('_dmarc.' + domain , 'TXT')
        for dns_data in test_dmarc:
            if 'DMARC1' in str(dns_data):
                print ("  [PASS] DMARC record found :",dns_data)
                return True
    except:
        print ("  [FAIL] DMARC record not found.")
    
    return False

def check_DKIM(domain, selector="mail"):
    # Testing DKIM
    print()
    print ("Testing domain", domain, "for DKIM record with selector", selector, "...")
    try:
        test_dkim = dns.resolver.resolve(selector + '._domainkey.' + domain , 'TXT')
        for dns_data in test_dkim:
            if 'DKIM1' in str(dns_data) or "k=rsa" in str(dns_data):
                print ("  [PASS] DKIM record found  :",dns_data)
                return True
    except:
        print ("  [FAIL] DKIM record not found.")
    
    return False

def check_SPF(domain):
    # Testing SPF
    print()
    print ("Testing domain", domain, "for SPF record...")
    try:
        test_spf = dns.resolver.resolve(domain , 'TXT')
        for dns_data in test_spf:
            if 'spf1' in str(dns_data):
                print ("  [PASS] SPF record found   :",dns_data)
                return True
    except:
        print ("  [FAIL] SPF record not found.")
    return False

def check_dds(domain, selector="mail"):
    """_summary_

    Args:
        domain (str): nyu.edu
        selector (str, optional): _description_. Defaults to "mail".

    Returns:
        _type_: [False, False, False]
    """
    spf = check_SPF(domain)
    dkim = check_DKIM(domain, selector)
    dmarc = check_DMARC(domain)
    return [spf, dkim, dmarc]

if __name__ == "__main__":
    nyu = "nyu.edu"
    usas = "mails.ucas.ac.cn"
    check_dds(usas)
    
    # check_DMARC(usas)