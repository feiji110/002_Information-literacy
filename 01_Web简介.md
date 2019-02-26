![2019/2/26 10:56:50 ](https://cn.bing.com/az/hprichbg/rb/WinterGrand_ZH-CN5111542555_1920x1080.jpg)
## 万维网『www(World Wide Web)』『Web』
	由许多互相链接的超文本组成的系统
## 访问页面过程
	Sever(服务器)---URL---Browser（浏览器输入地址发出申请）
## Web相关概念
	服务器：Apache和ngix
	URL(Uniform Resource Locator)
	+ 协议ftp-http-https
	+ 服务器地址（域名）『万维网上购买对应IP地址』
	+ 资源路径（首页通常隐藏）
## 网络应用程序架构

### B/S架构
	通过Browser访问的网络应用程序
	+ 速度慢，用户体验单一
	+ 无需安装，跨平台
	+ 官网，网页版QQ
### C/S架构
	通过客户端软件访问的网络应用程序
	+ 需要安装特定程序
	+ 能直接使用客户端硬件资源
	+ QQ
## Web历史
	1.0（信息共享）——>2.0（共建信息）——>3.0—（移动互联网）—>4.0（物联网，互联网+）
```
<script src="https://cdn.bootcss.com/raphael/2.2.7/raphael.min.js"></script>
<script src="https://cdn.bootcss.com/jquery/3.3.1/jquery.min.js"></script>
<script src="https://cdn.bootcss.com/flowchart/1.11.0/flowchart.js"></script>
<script>
        window.onload = function () {
            var ht = $('.lang-flow').html();
            $('.lang-flow').replaceWith('<textarea class="lang-flow">' + ht + '</textarea>');
            $('.lang-flow').parent().hide();
            /*
             * 追加canvas
             * */
            $('.lang-flow').parent().after('<div id="canvas"></div>');
            /*
             * 渲染
             * */
            var cd = document.getElementsByClassName("lang-flow"), chart;
            (cd.change = function () {
                var code = cd[0].value;
                if (chart) {
                    chart.clean();
                }
                chart = flowchart.parse(code);
                chart.drawSVG('canvas', {
//                     'x': 30,
//                     'y': 50,
                        'line-width': 3,
                        'maxWidth': 3,//ensures the flowcharts fits within a certian width
                        'line-length': 50,
                        'text-margin': 10,
                        'font-size': 14,
                        'font': 'normal',
                        'font-family': 'Helvetica',
                        'font-weight': 'normal',
                        'font-color': 'black',
                        'line-color': 'black',
                        'element-color': 'black',
                        'fill': 'white',
                        'yes-text': 'yes',
                        'no-text': 'no',
                        'arrow-end': 'block',
                        'scale': 1,
                        'symbols': {
                            'start': {
                                'font-color': 'red',
                                'element-color': 'green',
                                'fill': 'yellow'
                            },
                            'end': {
                                'class': 'end-element'
                            }
                        },
                        'flowstate': {
                            'past': {'fill': '#CCCCCC', 'font-size': 12},
                            'current': {'fill': 'yellow', 'font-color': 'red', 'font-weight': 'bold'},
                            'future': {'fill': '#FFFF99'},
                            'request': {'fill': 'blue'},
                            'invalid': {'fill': '#444444'},
                            'approved': {'fill': '#58C4A3', 'font-size': 12, 'yes-text': 'APPROVED', 'no-text': 'n/a'},
                            'rejected': {'fill': '#C45879', 'font-size': 12, 'yes-text': 'n/a', 'no-text': 'REJECTED'}
                        }
                    }
                );
            })();
        };
    
   
 $('.lang-flow').each( function(){
           var ht = $(this).html();
               $(this).replaceWith('<textarea class="lang-flow">' + ht + '</textarea>');
         });
         $('.lang-flow').each( function(index,element){
               $(this).parent().hide();
              $(this).parent().after('<div id="canvas'+index+'"></div>');
         });
            var cd = document.getElementsByClassName("lang-flow");
            (cd.change = function () {
              for(var i=0 ; i<cd.length ; i++){
               var code = cd[i].value;
                var chart = flowchart.parse(code);
                chart.drawSVG('canvas'+i, {
//                     'x': 30,
//                     'y': 50,
	 </script>
	
<link rel="stylesheet" href="https://cdn.bootcss.com/highlight.js/8.0/styles/solarized_dark.min.css">
<script src="https://cdn.bootcss.com/highlight.js/8.0/highlight.min.js"></script>
<script>hljs.initHighlightingOnLoad();</script>
<script src="https://cdn.bootcss.com/raphael/2.2.7/raphael.min.js"></script>
<script src="https://cdn.bootcss.com/jquery/3.3.1/jquery.min.js"></script>
<script src="https://cdn.bootcss.com/flowchart/1.11.0/flowchart.js"></script>
<script>
        window.onload = function () {
            var ht = $('.lang-flow').html();
            $('.lang-flow').replaceWith('<textarea class="lang-flow">' + ht + '</textarea>');
            $('.lang-flow').parent().hide();
            /*
             * 追加canvas
             * */
            $('.lang-flow').parent().after('<div id="canvas"></div>');
            /*
             * 渲染
             * */
            var cd = document.getElementsByClassName("lang-flow"), chart;
            (cd.change = function () {
                var code = cd[0].value;
                if (chart) {
                    chart.clean();
                }
                chart = flowchart.parse(code);
                chart.drawSVG('canvas', {
//                     'x': 30,
//                     'y': 50,
                        'line-width': 3,
                        'maxWidth': 3,//ensures the flowcharts fits within a certian width
                        'line-length': 50,
                        'text-margin': 10,
                        'font-size': 14,
                        'font': 'normal',
                        'font-family': 'Helvetica',
                        'font-weight': 'normal',
                        'font-color': 'black',
                        'line-color': 'black',
                        'element-color': 'black',
                        'fill': 'white',
                        'yes-text': 'yes',
                        'no-text': 'no',
                        'arrow-end': 'block',
                        'scale': 1,
                        'symbols': {
                            'start': {
                                'font-color': 'red',
                                'element-color': 'green',
                                'fill': 'yellow'
                            },
                            'end': {
                                'class': 'end-element'
                            }
                        },
                        'flowstate': {
                            'past': {'fill': '#CCCCCC', 'font-size': 12},
                            'current': {'fill': 'yellow', 'font-color': 'red', 'font-weight': 'bold'},
                            'future': {'fill': '#FFFF99'},
                            'request': {'fill': 'blue'},
                            'invalid': {'fill': '#444444'},
                            'approved': {'fill': '#58C4A3', 'font-size': 12, 'yes-text': 'APPROVED', 'no-text': 'n/a'},
                            'rejected': {'fill': '#C45879', 'font-size': 12, 'yes-text': 'n/a', 'no-text': 'REJECTED'}
                        }
                    }
                );
            })();
        };
         </script>
```
