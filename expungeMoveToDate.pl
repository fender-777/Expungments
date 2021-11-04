#!/usr/bin/perl
use strict;
use File::Copy;
use POSIX();

my @dirs = grep{-d} glob 'C:/Expungments/*';

foreach my $dir (@dirs) {
    print "Working directory $dir\n";
    chdir $dir or die "Can't change to $dir, $!\n";
    my @pdfFiles = glob("*.pdf");

    foreach my $pdf (@pdfFiles) {
#        print "Working pdf $pdf\n";
        my $mtime = (stat($pdf))[9];      
        my $ymString = POSIX::strftime("%Y%m", localtime($mtime)); # get the modified time, in seconds
        my $ymdString = POSIX::strftime("%Y%m%d", localtime($mtime));   # format the time to yyyymmdd

#        print "File:\t" . $pdf . 
#            ", Last Modified Date:\t" . $ymdString . ".\n";

        if (!-d $ymString) {
            # directory does not exist, make it first
#            print "Making $ymdString subdirectory.\n";
            mkdir("c:/expungments/$ymString");
        } #if YMD-named directory exists
        copy($pdf,"c:/Expungments/$ymString/$pdf"); # copy PDF from where it is to new YMD directory
        

    } # foreach PDF in this directory
} # foreach directory in c:\expungments


exit;
