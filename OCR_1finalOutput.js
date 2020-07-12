const fs = require('fs');
fs.readFile('Output.txt', (err, data) => {
    data = data.toString();
    portLoading = data.split('Port of Loading :')[1].slice(0, 20);
    totalPkgs = data.split('Total Pkgs. :')[1].slice(0, 6);
    portOfDischarge = data.split('Port of Discharge:')[1].slice(0, 6);
    loosePckts = data.split('Loose pckts :')[1].slice(0, 4);
    groossWeight = data.split('Gross Wt(KGS) :')[1].slice(1, 12);
    netWeight = data.split('Net Wt(KGS) :')[1].slice(0, 9);
    countryOfDest = data.split('Country of Dest')[1].slice(1, 15);
    noOfCtrs = data.split('No.of Ctrs. :')[1].slice(0, 4);
    console.log('PORT OF LOADING:', portLoading)
    console.log('Total Packages:', totalPkgs)
    console.log('Port of Discharge:', portOfDischarge)
    console.log('Loose Packets:', loosePckts)
    console.log('Gross Weight:', groossWeight);
    console.log('Net Weight:', netWeight);
    console.log('Country of Destination:', countryOfDest);
    console.log('No. of Ctrs:', noOfCtrs);
    // console.log(data.split('Port of Loading :')[1])
    if (err) {
        console.log(err);
    }
})