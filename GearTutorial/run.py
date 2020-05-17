import flywheel
context = flywheel.GearContext()  # Get the gear context
config = context.config           # from the gear context, get the config settings
## Load in values from the gear configuration
my_name = config['my_name']
num_rep = config['num_rep']

## Load in paths to input files for the gear
message_file = context.get_input_path('message_file')
#my_name = "Yichao Deng"       # The name we want to say hello to
#num_rep = 5                     # The number of times to say hello
#custom_message = "message.txt"  # A .txt file with a text message to print
while (num_rep > 0):                   # While the num_rep variable is greater than zero
   print("Hello, {}!".format(my_name)) # Print "Hello Name!" every loop
   num_rep -= 1                       # Decrease the num_rep variable by one

message_file = open(message_file,'r')   # Open the file with the intent to read
print('\n')                               # Print a blank line to separate the message from the "hello's"
#print('Custom Message:')
#print('\n')
print(message_file.read())                # Read and print the file