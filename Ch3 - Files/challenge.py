import os


def main():
    total_bytes = 0

    # get a list of all the files in the current directory
    dir_list = os.listdir()

    for entry in dir_list:

        # check if it is a file
        if os.path.isfile(entry):
            # add file size to the total
            file_size = os.path.getsize(entry)
            total_bytes += file_size

    #  create a subdirectory called "results"
    os.mkdir("results")

    # create the output file
    resultsfile = open("results/results.txt", "w+")
    if resultsfile.mode == "w+":
        resultsfile.write("Total byte count: " + str(total_bytes) + "\n")
        resultsfile.write("Files list:\n")
        resultsfile.write("----------------\n")
        for entry in dir_list:
            if os.path.isfile(entry):
                # write the file name to the results ledger
                resultsfile.write(entry + "\n")

    resultsfile.close()


if __name__ == "__main__":
    main()
