HEAD_HTML = """<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html
PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
"DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<head>
    <link rel="stylesheet" type="text/css" href="css/style-vis.css"/>
    <script type="text/javascript" src="js/head.js"></script>
    <title> View prodigy relations</title>
</head>

<body>
    <!-- Start BRAT (always static) -->
    <script type="text/javascript">
        var bratLocation = 'brat-v1.3_Crunchy_Frog';
        head.js(
        // External libraries
        bratLocation + '/client/lib/jquery.min.js',
        bratLocation + '/client/lib/jquery.svg.min.js',
        bratLocation + '/client/lib/jquery.svgdom.min.js',
        // brat helper modules
        bratLocation + '/client/src/configuration.js',
        bratLocation + '/client/src/util.js',
        bratLocation + '/client/src/annotation_log.js',
        bratLocation + '/client/lib/webfont.js',
        // brat modules
        bratLocation + '/client/src/dispatcher.js',
        bratLocation + '/client/src/url_monitor.js',
        bratLocation + '/client/src/visualizer.js'
        );
        var webFontURLs = [
            bratLocation + '/static/fonts/Astloch-Bold.ttf',
            bratLocation + '/static/fonts/PT_Sans-Caption-Web-Regular.ttf',
            bratLocation + '/static/fonts/Liberation_Sans-Regular.ttf'
        ];
    
    </script>

"""

END_HTML = """
</body>
</html>
"""

COLL_JS_VAR = """
var collData = 
{
    entity_types: [
    {type: 'PK',labels : ['PK', 'PK'], bgColor: '#ffa9b8',borderColor: 'darken'},
    {type: 'VALUE', labels : ['VALUE', 'V'], bgColor: '#d1caff', borderColor: 'darken'},
    {type: 'UNITS', labels : ['UNITS', 'U'],bgColor: '#00ffff',borderColor: 'darken'},
    {type: 'TYPE_MEAS',labels : ['TYPE_MEAS', 'T'],bgColor: '#ffa973',borderColor: 'darken'},
    {type: 'COMPARE', labels : ['COMPARE', 'COM'], bgColor: '#9effd6',borderColor: 'darken'},
    {type: 'RANGE', labels : ['RANGE', 'R'], bgColor: '#66f542',borderColor: 'darken'}       
    ],
    relation_types: [
    { type: 'C_VAL', labels: ['C_VAL', 'C'], color : 'blue'},
    { type: 'D_VAL', labels   : ['D_VAL', 'D'], color: '#ff8c00'},
    { type: 'RELATED', labels: ['RELATED', 'R'], color: '#32cd32',}
    ]
};
"""

