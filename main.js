import slideorama from "slideorama";

import hljs from 'highlight.js/lib/highlight';
import javascript from 'highlight.js/lib/languages/javascript';
import cpp from 'highlight.js/lib/languages/cpp';
import x86asm from 'highlight.js/lib/languages/x86asm';
hljs.registerLanguage('x86asm', x86asm);
hljs.registerLanguage('cpp', cpp);
hljs.registerLanguage('javascript', javascript);
import "highlight.js/styles/atom-one-dark.css";

slideorama.init("presentation", "slide-container");
hljs.initHighlightingOnLoad();
