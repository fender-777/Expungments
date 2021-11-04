#!/usr/bin/perl
use strict;
use File::Copy;
use POSIX();


#my @dirs = grep {-d} glob 'C:/Expungments/*';
my @dirs = grep {-d} glob './*';


foreach my $dir (@dirs) {
    if ($dir =~ m/\d{6}/) {
        print "Working directory $dir\n";
        chdir $dir or die "Can't change to $dir, $!\n";
        # one of our date directories
        my @pdfFiles = glob("*.pdf");
        my @nameArray;

        foreach my $pdf (@pdfFiles) {
            @nameArray = split(/\./,$pdf);
            if (!-e "${nameArray[0]}-0.jpg") {
                # if at least one image with this PDF name doesn't exist, we need to extract the images
                system("magick convert \"$pdf\" -density 1024 \"$pdf.jpg\"");
                my @jpgs = glob("*.jpg");
                open OUTFILE, ">" "tesseract_list.txt";
                foreach my $jpg (@jpgs) {
                    print OUTFILE "$jpg\n";
                }
                close OUTFILE;

                system("tesseract tesseract_list.txt $dir -l eng pdf");
#                system("dir *.jpg > jpgs.txt");
            }

        } # foreach PDF in this directory
    } # if one of our date directories
} # foreach directory
