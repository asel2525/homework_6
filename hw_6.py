# 1

try:
    file_name = input("Enter a file name: ")
    with open(file_name, 'r') as f:
        line_number = 1
        
        for i in f:
            print(f"LINE NUMBER : {line_number}")
            print(i.upper(), end='')
            line_number += 1

except FileNotFoundError:
    print(f"Error: File '{file_name}' not found")

except Exception as e:
    print(f"An error occurred: {e}")
    
# 2

hosts = set()
with open("mbox.txt", "r") as file:
  for line in file:
    if line.startswith("From:"):
      email_account = line.split()[1]
      host = email_account.split("@")[1]
      hosts.add(host)
      
for host in hosts:
  print(host)

print(f"Total {len(hosts)} hosts printed")

# 3

try:
    file_name = input("Enter a file name: ")
    scores = []
    
    with open(file_name, "r") as file:
        for i in file:
            if i.startswith("X-DSPAM-Confidence: "):
                score = float(i.split(":")[1])
                scores.append(score)
                
except FileNotFoundError:
    print(f"Error: File '{file_name}' not found")
    
if not scores:
    print("No emails found in file.")
    exit()

average_score = sum(scores) / len(scores)

print(f"Average spam confidence: {average_score}")
    
