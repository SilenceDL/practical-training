**Xpath学习文档**

    XPath 是一门在 XML 文档中查找信息的语言。XPath 用于在 XML 文档中通过元素和属性进行导航。
    
    在学习之前应该具备的知识：
    在您继续学习之前，应该对下面的知识有基本的了解：    
    HTML / XHTML
    XML / XML 命名空间
   
    什么是 XPath?
    XPath 使用路径表达式在 XML 文档中进行导航
    XPath 包含一个标准函数库
    XPath 是 XSLT 中的主要元素
    XPath 是一个 W3C 标准
    XPath 路径表达式
    XPath 使用路径表达式来选取 XML 文档中的节点或者节点集。这些路径表达式和我们在常规的电脑文件系统中看到的表达式非常相似。
    
        表达式	描述
    nodename	选取此节点的所有子节点。
    /	从根节点选取。
    //	从匹配选择的当前节点选择文档中的节点，而不考虑它们的位置。
    .	选取当前节点。
    ..	选取当前节点的父节点。
    @	选取属性。
    
    例子：
    路径表达式	结果
    bookstore	选取 bookstore 元素的所有子节点。
    /bookstore	
    选取根元素 bookstore。   
    注释：假如路径起始于正斜杠( / )，则此路径始终代表到某元素的绝对路径！ 
    bookstore/book	选取属于 bookstore 的子元素的所有 book 元素。
    //book	选取所有 book 子元素，而不管它们在文档中的位置。
    bookstore//book	选择属于 bookstore 元素的后代的所有 book 元素，而不管它们位于 bookstore 之下的什么位置。
    //@lang	选取名为 lang 的所有属性。