---
id: 1475
title: "נוסחת ההיפוך של מביוס"
date: 2012-01-07 13:08:03
layout: post
categories: 
  - קומבינטוריקה
  - תורת המספרים
tags: 
  - נוסחת ההיפוך של מביוס
  - קבוצות סדורות חלקית
---
<h2><strong>נוסחת ההיפוך הקלאסית</strong></h2>
נתחיל מדוגמה. ככה יהיה הרבה יותר קל להבין מה אני רוצה. בפוסט הקודם הזכרתי את <strong>פונקציית אוילר</strong> {% equation %}\varphi\left(n\right){% endequation %} שלכל מספר טבעי מחזירה את מספר המספרים הקטנים ממנו שזרים לו. בנוסף לכל מעלותיה, היא מקיימת את התכונה היפה הבאה: {% equation %}\sum_{d|n}\varphi\left(d\right)=n{% endequation %}. כלומר, כל מספר טבעי שווה לסכום הערכים של פונקציית אוילר כל כל מחלקיו.

לנוסחה הזו יש הוכחה קומבינטורית פשוטה שלחלוטין לא רלוונטית לפוסט אז העצלנים יכולים לדלג עליה - נספור את כל המספרים מ-1 עד {% equation %}n{% endequation %} (בדיוק {% equation %}n{% endequation %}) בדרך קצת שונה - לכל מספר {% equation %}1\le k\le n{% endequation %}, נסמן ב-{% equation %}N_{k}{% endequation %} את מספרם של המספרים בין 1 ו-{% equation %}n{% endequation %} שהמחלק המשותף המקסימלי שלהם ושל {% equation %}n{% endequation %} הוא בדיוק {% equation %}k{% endequation %}, כלומר {% equation %}N_{k}=\left|\left\{ 1\le a\le n|\gcd\left(a,n\right)=k\right\} \right|{% endequation %}. בבירור אם {% equation %}k{% endequation %} לא מחלק את {% equation %}n{% endequation %} אז {% equation %}N_{k}=0{% endequation %}; מהו {% equation %}N_{k}{% endequation %} אם {% equation %}k|n{% endequation %}? ובכן, זהו מספרם של המספרים מהצורה {% equation %}k,2k,3k,\dots,n{% endequation %} שאין להם מחלק משותף גדול מ-{% equation %}k{% endequation %} עם {% equation %}n{% endequation %}, כלומר מספרים מהצורה {% equation %}tk{% endequation %} כך ש-{% equation %}t{% endequation %} זר ל-{% equation %}\frac{n}{k}{% endequation %} (תעצרו, תנשמו עמוק ותסבירו את זה לעצמכם - אם אתם לא מצליחים, לא נורא כי זה לא קשור ממש לפוסט). נסמן {% equation %}d=\frac{n}{k}{% endequation %} ונקבל ש-{% equation %}N_{k}=\varphi\left(d\right){% endequation %}, ומכאן נובעת הנוסחה.

יופי, בשביל מה זה היה טוב? ובכן, זו דוגמה לסיטואציה שבה יש לנו פונקציה מסובכת {% equation %}f{% endequation %} שסכום שלה על פני המחלקים של {% equation %}n{% endequation %} יוצא משהו פשוט יותר. פורמלית, זה אומר שקיימת פונקציה {% equation %}g\left(n\right){% endequation %} כך ש-{% equation %}g\left(n\right)=\sum_{d|n}f\left(d\right){% endequation %}. היינו רוצים איכשהו "לחלץ" את {% equation %}f{% endequation %} מתוך הנוסחה הזו ולכתוב אותה כפונקציה כלשהי של {% equation %}g{% endequation %} הפשוטה יותר. נוסחת ההיפוך של מביוס נותנת לנו בדיוק את זה.

אפשר עכשיו פשוט להציג את הנוסחה, אבל חבל - אני רוצה לנצל את ההזדמנות כדי להכיר לכם מושג חדש, שממנו אפשר יהיה להגיע לנוסחה באופן טבעי יותר - קונבולוציית דיריכלה. קונבולוציה "רגילה" של שתי פונקציות {% equation %}f,g{% endequation %} שמוגדרות על הטבעיים היא פונקציה חדשה {% equation %}h{% endequation %} שמוגדרת כך: {% equation %}h\left(n\right)=\sum_{k=0}^{n}f\left(k\right)g\left(n-k\right){% endequation %}. דוגמה קלאסית לסיטואציה מתמטית שבה קונבולוצייה רגילה צצה מאליה היא כפל של פולינומים: אם {% equation %}p\left(x\right)=\sum a_{i}x^{i}{% endequation %} ו-{% equation %}q\left(x\right)=\sum b_{j}x^{j}{% endequation %} אז כל מקדם של המכפלה שלהם הוא קונבולוציה: המקדם של {% equation %}x^{n}{% endequation %} ב-{% equation %}p\left(x\right)q\left(x\right){% endequation %} הוא {% equation %}\sum_{k=0}^{n}a_{k}b_{n-k}{% endequation %}. שימו לב, שניתן לכתוב קונבולוציה גם עם חיבור ולא חיסור: {% equation %}h\left(n\right)=\sum_{k+r=n}f\left(k\right)g\left(r\right){% endequation %}.

קונבולוציית דיריכלה היא דומה באופיה, רק שבמקום חיבור/חיסור משתמשים בכפל/חילוק, דהיינו אם {% equation %}h\left(n\right){% endequation %} היא קונבולוציית דיריכלה של {% equation %}f\left(n\right),g\left(n\right){% endequation %} אז

{% equation %}h\left(n\right)=\sum_{d\cdot e=n}f\left(d\right)g\left(e\right)=\sum_{d|n}f\left(d\right)g\left(\frac{n}{d}\right){% endequation %}

זה כבר טיפה מזכיר את מה שהלך למעלה.

בואו נסמן {% equation %}h=f*g{% endequation %} כדי לומר ש-{% equation %}h{% endequation %} היא קונבולוציית דיריכלה של {% equation %}f,g{% endequation %}. אז האלגבראיסט הפנימי שבנו מתלהב מכך שמצאנו פעולה חשבונית חדשה ודוחק בנו לחקור את התכונות שלה. למשל, {% equation %}\left(f*g\right)*h=f*\left(g*h\right){% endequation %} עבור שלוש פונקציות {% equation %}f,g,h{% endequation %} כלשהן (שמוגדרות על טבעיים; זה תמיד ההקשר של הדיון), כך שקונבלוציית דיריכלה היא <strong>אסוציאטיבית</strong>. זה מגביר את ההתלהבות של האלגבראיסט הפנימי לשמיים כי הוא מקווה שיש לנו כאן <strong>חבורה</strong>, כלומר מבנה אלגברי שהפעולה שלו היא אסוציאטיבית, עם איבר יחידה, ועם הופכי לכל איבר. ובכן, איבר יחידה בהחלט יש: נסמן ב-{% equation %}\epsilon{% endequation %} את הפונקציה שמקיימת {% equation %}\epsilon\left(1\right)=1{% endequation %} ו-{% equation %}\epsilon\left(n\right)=0{% endequation %} לכל {% equation %}n&gt;1{% endequation %}, אז קל מאוד לראות מההגדרה ש-{% equation %}\epsilon*f=f*\epsilon=f{% endequation %}.

וכעת, מה עם הופכי? ובכן, נניח שעבור {% equation %}f{% endequation %} קיימת {% equation %}g{% endequation %} כך ש-{% equation %}f*g=\epsilon{% endequation %}, זה אומר ש-{% equation %}\sum_{d|1}f\left(d\right)g\left(\frac{n}{d}\right)=1{% endequation %}, כלומר {% equation %}f\left(1\right)g\left(1\right)=1{% endequation %}; אבל אם {% equation %}f\left(1\right)=0{% endequation %} אז אבוד לנו - המשוואה הזו לעולם לא תתקיים. לכן תנאי הכרחי לכך ש-{% equation %}f{% endequation %} יהיה הפיך הוא ש-{% equation %}f\left(1\right)\ne0{% endequation %}. מסתבר שזה גם תנאי מספיק, אבל נעזוב את החיפוש אחר הופכי במקרה הכללי כרגע ובמקום זאת נתמקד בהופכי של פונקציה פשוטה במיוחד: הפונקציה שמחזירה 1 לכל קלט, שאסמן פשוט כ-{% equation %}\mathbb{I}{% endequation %}. את ההופכי שלה, שתכף נוכיח את קיומו, נסמן ב-{% equation %}\mu{% endequation %} מסיבות היסטורית. אם כן, {% equation %}\mathbb{I}*\mu=\epsilon{% endequation %}. בואו נראה מה נובע מכך.

זכרו שהתחלנו את כל הסיפור מהמשוואה {% equation %}g\left(n\right)=\sum_{d|n}f\left(d\right){% endequation %}. עם הטרמינולוגיה החדשה שלנו ניתן לנסח זאת בתור {% equation %}g=f*\mathbb{I}{% endequation %}. כעת נכפול את שני האגפים ב-{% equation %}\mu{% endequation %}, נשתמש באסוציאטיביות, ונקבל:

{% equation %}g*\mu=f*\left(\mathbb{I}*\mu\right)=f*\epsilon=f{% endequation %}

במילים אחרות, {% equation %}g=f*\mathbb{I}{% endequation %} אם ורק אם {% equation %}f=g*\mu{% endequation %}, ובניסוח המקורי שלנו {% equation %}g\left(n\right)=\sum_{d|n}f\left(d\right){% endequation %} אם ורק אם {% equation %}f\left(n\right)=\sum_{d|n}g\left(d\right)\mu\left(\frac{n}{d}\right){% endequation %}. זוהי <strong>נוסחת ההיפוך של מביוס</strong>, והפונקציה {% equation %}\mu{% endequation %} נקראת, בהתאם, <strong>פונקצית מביוס</strong>. בואו נבין איך היא נראית.

ראשית, {% equation %}\mu\left(1\right)=1{% endequation %} בבירור על פי ההגדרה, כי צריך שיתקיים {% equation %}\mu\left(1\right)\mathbb{I}\left(1\right)=1{% endequation %}. שנית, לכל {% equation %}n&gt;1{% endequation %} צריך שיתקיים {% equation %}0=\epsilon\left(n\right)=\sum_{d|n}\mu\left(d\right)\mathbb{I}\left(\frac{n}{d}\right)=\sum_{d|n}\mu\left(d\right){% endequation %}. כלומר, אם לסכם באופן קומפקטי, פונקציית מביוס חייבת לקיים {% equation %}\sum_{d|n}\mu\left(d\right)=\delta_{1n}{% endequation %}. מכאן אפשר להסיק בשלבים איך {% equation %}\mu{% endequation %} נראית על כל מספר טבעי. נתחיל מהמספרים הקלים ביותר לטיפול בהקשר הזה (כמו שקורה לעתים קרובות ביותר בתורת המספרים) - ראשוניים, אם {% equation %}d|p{% endequation %} עבור {% equation %}p{% endequation %} ראשוני, אז {% equation %}d=1{% endequation %} או {% equation %}d=p{% endequation %}, ולכן הנוסחה שלעיל מתורגמת עבורנו ל-{% equation %}0=\mu\left(1\right)+\mu\left(p\right){% endequation %}, כלומר {% equation %}\mu\left(p\right)=-1{% endequation %} לכל ראשוני. אפשר להמשיך ולטפל בצורה דומה במכפלות של ראשוניים, אבל אני לא מכיר דרך אלגנטית במיוחד להציג את הניתוח הזה ולכן אקפוץ למסקנה הסופית: {% equation %}\mu{% endequation %} היא כפלית על מספרים זרים. מה זה אומר? שאם {% equation %}a,b{% endequation %} הם שני מספרים ללא מחלק משותף גדול מ-1, אז {% equation %}\mu\left(ab\right)=\mu\left(a\right)\mu\left(b\right){% endequation %} (באופן הולם למדי, גם {% equation %}\varphi{% endequation %} של אוילר היא כזו). ומה אם {% equation %}a,b{% endequation %} לא זרים? גם אז המצב פשוט: {% equation %}\mu\left(ab\right)=0{% endequation %}.

כעת אפשר להסיק נוסחה עבור {% equation %}\mu{% endequation %}. נניח ש-{% equation %}n=p_{1}p_{2}\cdots p_{k}{% endequation %} כאשר כל הראשוניים הללו שונים זה מזה, אז {% equation %}\mu\left(n\right)=\prod_{i=1}^{k}\mu\left(p_{k}\right)=\left(-1\right)^{k}{% endequation %}; ואילו אם {% equation %}n{% endequation %} מכיל את אותו ראשוני פעמיים בפירוק שלו, {% equation %}\mu\left(n\right)=0{% endequation %}.

לא קשה לראות שאכן {% equation %}\sum_{d|n}\mu\left(d\right)=0{% endequation %} בהגדרה זו לכל {% equation %}n&gt;0{% endequation %}; אם {% equation %}n=p_{1}^{t_{1}}\cdots p_{k}^{t_{k}}{% endequation %} הרי שהסכום יהיה רק על מחלקים {% equation %}d{% endequation %} מהצורה {% equation %}p_{1}^{e_{1}}\cdots p_{k}^{e_{k}}{% endequation %} עם {% equation %}e_{i}\in\left\{ 0,1\right\} {% endequation %} (כי היתר יתאפסו), ועבור כל מכפלה כזו, {% equation %}\mu\left(p_{1}^{e_{1}}\cdots p_{k}^{e_{k}}\right){% endequation %} שווה למינוס 1 בחזקת מספר ה-{% equation %}e_{i}{% endequation %}-ים שהם 1, ולכן {% equation %}\sum_{d|n}\mu\left(d\right)=\sum_{i=0}^{k}{k \choose i}\left(-1\right)^{i}=\left(1-1\right)^{k}=0{% endequation %} (המעבר האחרון הוא הבינום של ניוטון). כלומר, {% equation %}\mu{% endequation %} שנתתי אכן מקיימת את מה שנדרש ממנה, וזה מבטיח שהיא אכן תהיה ההופכית של {% equation %}\mathbb{I}{% endequation %} ושנוסחת ההיפוך של מביוס תתקיים.

יפה, זה סוגר את העניין בכל הנוגע לנוסחת ההיפוך ה"קלאסית" של מביוס, זו שרואים בספרי תורת המספרים. אבל יש כאן יותר מזה. נתחיל מלהיזכר במה שראינו על ההכללה של עקרון ההכלה וההפרדה בפוסט הקודם. שם היו לנו שתי פונקציות {% equation %}f,g{% endequation %} כך שהתקיים

{% equation %}g\left(A\right)=\sum_{B\supseteq A}f\left(B\right){% endequation %}

ואת הנוסחה הזו "הפכנו" לקבלת

{% equation %}f\left(A\right)=\sum_{B\supseteq A}\left(-1\right)^{\left|B-A\right|}g\left(B\right){% endequation %}

הדמיון כאן לנוסחת ההיפוך של מביוס אדיר. במקום {% equation %}d|n{% endequation %} יש לנו {% equation %}B\supseteq A{% endequation %} כש-{% equation %}B{% endequation %} על תקן {% equation %}d{% endequation %} ו-{% equation %}A{% endequation %} על תקן {% equation %}n{% endequation %}, ובמקום {% equation %}\mu\left(d\right){% endequation %} יש לנו {% equation %}\left(-1\right)^{\left|B-A\right|}{% endequation %}, אבל זה כל ההבדל. המבנה הרעיוני זהה. יתר על כן, הדמיון בין חלוקה והכלה של קבוצות הוא משהו שכבר ראינו בבלוג פעם, בהקשר של תורת המספרים האלגברית; אם נגדיר את {% equation %}A{% endequation %} כקבוצת "כל המספרים המתחלקים על ידי {% equation %}n{% endequation %}" ואת {% equation %}B{% endequation %} כקבוצת "כל המספרים המתחלקים על ידי {% equation %}d{% endequation %}" אז {% equation %}B\supseteq A{% endequation %} <strong>שקול</strong> לאמירה {% equation %}d|n{% endequation %} (אבל אז לא ברור מהו {% equation %}\left|B-A\right|{% endequation %} שיהיה אינסופי). הדמיון הרב מאוד בין שני המקרים לא נגמר בהם; הוא נובע מכך ששניהם מקרים פרטיים של נוסחת היפוך כללית ביותר, שתקפה לכל מבנה מתמטי שמכליל את התכונות של "הכלה" או של "חלוקה" שרלוונטיות לעניינו - ולמבנה כזה קוראים <strong>קבוצה סדורה חלקית</strong> (קס"ח).
<h2><strong>קס"חים</strong></h2>
קבוצות סדורות חלקית הן מהמבנים הבסיסיים ביותר במתמטיקה, והצורה הפשוטה ביותר שבה אנו מתארים את הרעיון של <strong>סדר</strong>. בואו ניתן את ההגדרות האבסטרקטיות התורת-קבוצתיות: קבוצה {% equation %}X{% endequation %} הוא סדורה חלקית עם יחס שמסומן ב-{% equation %}\le{% endequation %} (יחס כאן הוא אוסף של זוגות {% equation %}\left(a,b\right){% endequation %} כך ש-{% equation %}a\in X{% endequation %} וגם {% equation %}b\in X{% endequation %}; אנחנו מסמנים {% equation %}a\le b{% endequation %}) אם {% equation %}\le{% endequation %}מקיים את שלוש התכונות הבאות:
<ol>
	<li> (רפלקסיביות) {% equation %}a\le a{% endequation %} לכל {% equation %}a\in X{% endequation %}</li>
	<li> (אנטי-סימטריה) {% equation %}a\le b{% endequation %} וגם {% equation %}b\le a{% endequation %} גורר {% equation %}a=b{% endequation %}</li>
	<li> (טרנזיטיביות) {% equation %}a\le b{% endequation %} וגם {% equation %}b\le c{% endequation %} גורר {% equation %}a\le c{% endequation %}</li>
</ol>
צריך מייד להבהיר ש-{% equation %}\le{% endequation %} הוא <strong>סימון</strong> של היחס. זה <strong>לא</strong> "גדול או שווה" במשמעות הרגילה שלו. מה שכן, היחס "גדול או שווה" הוא יחס סדר חלקי, אולי אחד מהפשוטים ביותר, ומכאן הסימון. אם כן, {% equation %}\mathbb{N}{% endequation %} עם יחס הסדר "גדול או שווה מ-" היא דוגמה לקבוצה סדורה חלקית; אבל {% equation %}\mathbb{N}{% endequation %} עם יחד הסדר "מחלק את", כלומר אם {% equation %}a|b{% endequation %} מסמנים זאת {% equation %}a\le b{% endequation %} היא דוגמה מעניינת הרבה יותר. ברור שזה אכן יחס סדר חלקי כי {% equation %}a|a{% endequation %} לכל {% equation %}a\in\mathbb{N}{% endequation %}, וגם שתי התכונות האחרות נובעות די בקלות מההגדרות; אבל בניגוד ליחס הקטן-או-שווה הרגיל, עבור יחס החלוקה יש לנו איברים ש<strong>אינם ניתנים להשוואה</strong>. למשל, 2 ו-3 לא מחלקים זה את זה ולכן לא מתקיים לא {% equation %}2\le3{% endequation %} וגם לא {% equation %}3\le2{% endequation %} עבור יחס סדר זה. קבוצה סדורה חלקית שבה כל שני איברים כן ניתנים להשוואה נקראת קבוצה סדורה <strong>מלאה</strong>, או <strong>סדורה לינארית</strong>.

שימו לב שקס"ח היא <strong>זוג</strong> - צריך לציין גם את {% equation %}X{% endequation %} וגם את {% equation %}\le{% endequation %}, כי על אותו {% equation %}X{% endequation %} אפשר להגדיר הרבה יחסי סדר שונים. למרות זאת רוב הזמן אני אכתוב כאן "קס"ח {% equation %}X{% endequation %}" ותו לא, מתוך הנחה שמה שאני אומר תקף <strong>לכל</strong> יחס סדר חלקי שנצמיד ל-{% equation %}X{% endequation %} (לפעמים עם דרישות נוספות שאציין).

אם יש לנו קבוצה {% equation %}X{% endequation %} כלשהי, אז אפשר להגדיר על אוסף תת-הקבוצות שלה {% equation %}P\left(X\right){% endequation %} יחס סדר על ידי הכלה (כלומר, לכל {% equation %}A,B\subseteq X{% endequation %} מגדירים {% equation %}A\le B{% endequation %} אם {% equation %}A\subseteq B{% endequation %}), וגם, באופן מעניין, על ידי הכלה הפוכה, כלומר {% equation %}A\le B{% endequation %} אם {% equation %}B\supseteq A{% endequation %} (אומרים שהקס"ח שסדורה על ידי הכלה הפוכה <strong>דואלית</strong> לזו שסדורה על ידי הכלה רגילה; אפשר להגדיר דואלי שבו יחס הסדר מתהפך לכל קס"ח). אם כן, המושג של יחס סדר חלקי תופס את ה"עולם" שבו מתקיימות שתי הנוסחאות שהצגתי למעלה, ועכשיו נותר רק לברר איך נראית הנוסחה הכללית ביותר. כדי לספק את הסקרנות שלכם אני אציג אותה כבר עכשיו, ואז נוכל לחשוב איך להציג אותה בצורה <strong>מעניינת</strong>, על ידי הבנה טובה יותר של קבוצות סדורות חלקית (המטרה שלנו תהיה להכליל במובן מסויים את גישת הקונבולוציה של נוסחת ההיפוך הקלאסית).

ובכן, נוסחת ההיפוך הכללית אומרת שאם {% equation %}\left(X,\le\right){% endequation %} היא קבוצה סדורה חלקית עם יחס הסדר {% equation %}\le{% endequation %} אשר מקיימת תכונת סופיות מסויימת (כל אידאל סדר ראשי הוא סופי - זה יתבהר בהמשך) אז אם יש לנו שתי פונקציות {% equation %}f,g:X\to\mathbb{C}{% endequation %} אשר מקיימות {% equation %}g\left(x\right)=\sum_{y\le x}f\left(y\right){% endequation %}, אז מתקיים {% equation %}f\left(x\right)=\sum_{y\le x}g\left(y\right)\mu\left(y,x\right){% endequation %}, כאשר {% equation %}\mu{% endequation %} היא פונקצית מביוס של הקס"ח {% equation %}X{% endequation %}. איך בדיוק היא מוגדרת - גם את זה נבין בהמשך. לכל קס"ח יש את פונקצית המביוס שלו, וכבר ראינו שתיים: את זו של הקס"ח עם יחס החלוקה, שהייתה {% equation %}\mu{% endequation %} הקלאסית; ואז זו של הקס"ח עם יחס ההכלה ההפוך של קבוצות, שקיימה {% equation %}\mu\left(B,A\right)=\left(-1\right)^{\left|B-A\right|}{% endequation %}.

מכיוון שאני רוצה להציג את נוסחת ההיפוך ופונקצית מביוס כנובעים מרעיון עמוק יותר, מעין הכללה של קונבולוציית דיריכלה, אני צריך לתת עוד כמה הגדרות שקשורות לקס"חים. ראשית, לכל שני איברים {% equation %}x,y\in X{% endequation %} אפשר להגדיר את ה<strong>קטע</strong> {% equation %}\left[x,y\right]=\left\{ z\in X|x\le z\le y\right\} {% endequation %}, כלומר כל האיברים שניתנים להשוואה עם {% equation %}x,y{% endequation %} ונמצאים ביניהם, כולל הם עצמם. אם אין אף איבר בין {% equation %}x{% endequation %} ל-{% equation %}y{% endequation %}, כלומר {% equation %}\left[x,y\right]=\left\{ x,y\right\} {% endequation %}, אומרים ש-{% equation %}y{% endequation %} <strong>מכסה</strong> את {% equation %}x{% endequation %}. על {% equation %}X{% endequation %} אומרים שהיא סופית מקומית אם כל קטע ב-{% equation %}X{% endequation %} הוא סופי (כך למשל {% equation %}\mathbb{Z}{% endequation %} עם יחס הסדר הרגיל היא סופית מקומית, אבל {% equation %}\mathbb{Q}{% endequation %} עם אותו יחס סדר בדיוק איננה).

<strong>שרשרת</strong> היא פשוט קבוצה של איברים ב-{% equation %}X{% endequation %} שכולם ניתנים להשוואה זה עם זה (תת-קבוצה סדורה מלאה של {% equation %}X{% endequation %}), ושמה מגיע מכך שאפשר לכתוב את איבריה כ-{% equation %}x_{1}\le x_{2}\le\dots\le x_{n}{% endequation %} (במקרה שבו השרשרת סופית, אבל ממילא רק זה יעניין אותנו כאן). <strong>אנטי-שרשרת</strong> היא בדיוק ההפך מכך - קבוצה של איברים ב-{% equation %}X{% endequation %} שלא ניתן להשוות אף זוג מהם - למשל, אם ניקח את הטבעיים עם יחס החלוקה, אז כל קבוצה של ראשוניים היא אנטי-שרשרת.

<strong>אידאל סדר</strong> {% equation %}I{% endequation %} הוא תת-קבוצה של {% equation %}X{% endequation %} בעלת התכונה שאם {% equation %}x\in I{% endequation %} ו-{% equation %}y\le x{% endequation %} אז {% equation %}y\in X{% endequation %} (מי שמכיר קצת אלגברה מופשטת ודאי רואה את הדמיון להגדרה ה"קלאסית" של אידאל). יש קשר בין אידאלי סדר ואנטי-שרשראות: אם ניקח את כל האיברים המקסימליים באידאל סדר {% equation %}I{% endequation %} כלשהו (איברים {% equation %}x\in I{% endequation %} כך שלא קיים {% equation %}y\in I{% endequation %} כך ש-{% equation %}x\le y{% endequation %}) אז נקבל אנטי-שרשרת, ומצד שני אם ניקח אנטי-שרשרת {% equation %}A{% endequation %} ונגדיר {% equation %}I=\left\{ y\in X|\exists x\in A,y\le x\right\} {% endequation %} נקבל אידאל סדר, ואם {% equation %}X{% endequation %} סופית זה נותן לנו התאמה חח"ע ועל בין אנטי-שרשרות ואידאלי סדר. באופן כללי אם בהינתן {% equation %}A{% endequation %} מגדירים ממנה {% equation %}I{% endequation %} כפי שתיארתי כאן, אז אומרים ש-{% equation %}A{% endequation %} <strong>יוצרת</strong> את האידאל {% equation %}I{% endequation %}; ואידאל {% equation %}I{% endequation %} הוא אידאל סדר <strong>ראשי</strong> אם הוא נוצר בדיוק על ידי איבר אחד, כלומר קיים {% equation %}x\in A{% endequation %} כך ש-{% equation %}I=\left\{ y\le x|y\in X\right\} {% endequation %}. במקרה הזה מסמנים לעתים {% equation %}I=\left\langle x\right\rangle {% endequation %}. שוב, למי שבקיא באלגברה מופשטת הדמיון לאידאלים "קלאסיים" מאוד ברור כאן.
<h2><strong>קונבולוצייה והיפוך, הגרסה המוכללת</strong></h2>
אוקיי, הגענו לאקשן. בואו ניקח קבוצה סדורה חלקית {% equation %}X{% endequation %} שהיא סופית מקומית, ונגדיר פונקציות על קבוצת <strong>כל הקטעים</strong> ב-{% equation %}X{% endequation %} (פונקציות ממשיות, אבל אפשר גם עבור שדות אחרים). במילים אחרות, פונקציות שנראות ככה: {% equation %}f\left(\left[x,y\right]\right){% endequation %}. לצורך פשטות אפשר לחשוב עליהן כפונקציות בשני משתנים: {% equation %}f\left(x,y\right){% endequation %}, אבל הכרחי שיתקיים {% equation %}x\le y{% endequation %} אחרת אין משמעות ל-{% equation %}\left[x,y\right]{% endequation %}.

בין כל זוג פונקציות כזה אפשר להגדיר פעולת כפל שתכליל את קונבולוציית דיריכלה, אבל נמאס לי מהכוכב המעצבן הזה אז אני פשוט אשתמש בסימון הסטנדרטי לכפל: שום סימון. אם {% equation %}f,g{% endequation %} הן פונקציות מקבוצת הקטעים של {% equation %}X{% endequation %} אל {% equation %}\mathbb{R}{% endequation %}, אז נגדיר:

{% equation %}fg\left(x,y\right)=\sum_{x\le z\le y}f\left(x,z\right)g\left(z,y\right){% endequation %}

כאן העובדה ש-{% equation %}X{% endequation %} סופית מקומית היא קריטית; אחרת הסכום הזה לא בהכרח היה סופי.

בואו נראה איך המושג הזה מכליל את זה של תחילת הפוסט. שם התעסקנו עם פונקציות שמוגדרות על הטבעיים; כאן {% equation %}X=\mathbb{N}{% endequation %} ויחס הסדר הוא חלוקה, כלומר {% equation %}a\le b{% endequation %} פירושו {% equation %}a|b{% endequation %}. כעת, אם {% equation %}f{% endequation %} היא פונקציה שמוגדרת על הטבעיים, אפשר להגדיר אותה גם על קטעים באופן הבא: {% equation %}f\left(a,b\right)=f\left(\frac{b}{a}\right){% endequation %} (זכרו: בגלל ש-{% equation %}\left[a,b\right]{% endequation %} הוא קטע, {% equation %}a\le b{% endequation %} ולכן {% equation %}a|b{% endequation %}). לכן בפרט {% equation %}f\left(a\right)=f\left(1,a\right){% endequation %}, ומההגדרה למעלה נקבל:

{% equation %}fg\left(n\right)=fg\left(1,n\right)=\sum_{1|d|n}f\left(1,d\right)g\left(d,n\right)=\sum_{d|n}f\left(d\right)g\left(\frac{n}{d}\right){% endequation %}

הופה! בדיוק ההגדרה של קונבולוציית דיריכלה.

אפשר להגדיר {% equation %}\epsilon{% endequation %} כמו קודם: {% equation %}\epsilon\left(x,x\right)=1{% endequation %} לכל {% equation %}x\in X{% endequation %}, ולכל {% equation %}x\ne y{% endequation %} {% equation %}\epsilon\left(x,y\right)=0{% endequation %} (למעשה, {% equation %}\delta{% endequation %} מתאים פה יותר, למי שזוכר את הדלתא של קרונקר, אבל לא חשוב). לא קשה לראות ש-{% equation %}\epsilon{% endequation %} היא איבר יחידה ביחס לכפל הפונקציות שהגדרתי לעיל. גם לא קשה לראות שהכפל אסוציאטיבי.

את מקומה של הפונקציה שסימנתי אז {% equation %}\mathbb{I}{% endequation %} תופסת עכשיו פונקציית זטא: {% equation %}\zeta\left(x,y\right)=1{% endequation %} לכל {% equation %}x\le y{% endequation %}. רגע, למה זטא? אודה ואתוודה - לא יודע, אני לא בטוח מה הקשר של הפונקציה הזו לשאר פונקציות הזטא הקיימות, אבל אלו הסימונים. באופן בלתי מפתיע, מגדירים כעת את פונקצית מביוס של הקס"ח {% equation %}X{% endequation %} בתור ההופכית של {% equation %}\zeta{% endequation %}, כלומר {% equation %}\zeta\mu=\mu\zeta=\epsilon{% endequation %}. כעת, נוסחת ההיפוך של מביוס, בתיאורה האבסטרקטי ביותר, היא פשוט האבחנה הסופר-טריוויאלית ש- {% equation %}f\zeta=g{% endequation %} אם ורק אם {% equation %}f=g\mu{% endequation %} (רק שיש כאן טוויסט כאן שתכף אסביר).

קרוב לודאי שאתם מרגישים שיצאתי יותר מדי בזול מכל העניין. איפה אני מוכיח משהו, בכלל? אתם כמובן צודקים - מה שחסר לי הוא הוכחה ש-{% equation %}\zeta{% endequation %}הפיכה בכלל. כדי לטפל בכך אוכיח משהו כללי יותר - שפונקציה {% equation %}f{% endequation %} היא הפיכה אם ורק אם {% equation %}f\left(x,x\right)\ne0{% endequation %} לכל {% equation %}x\in X{% endequation %}. חזרנו אל "החיפוש אחרי הופכי במקרה הכללי" של תחילת הפוסט, רק שהפעם אני לא הולך להתחמק.

למרבה המזל, האתגר לא גדול במיוחד. נתונה לי {% equation %}f{% endequation %} ואני רוצה למצוא {% equation %}g{% endequation %} כך ש-{% equation %}fg=\epsilon{% endequation %}. כלומר, כך ש-{% equation %}fg\left(x,x\right)=\epsilon\left(x,x\right)=1{% endequation %} לכל {% equation %}x{% endequation %}, ומכיוון שעל פי הגדרה {% equation %}fg\left(x,x\right)=f\left(x,x\right)g\left(x,x\right){% endequation %}, הרי ש-{% equation %}g\left(x,x\right)=\left(f\left(x,x\right)\right)^{-1}{% endequation %} (כאן אני נעזר בכך שהערכים שהפונקציות מקבלות שייכים ל<strong>שדה</strong>), ואנו רואים גם למה הכרחי שיתקיים {% equation %}f\left(x,x\right)\ne0{% endequation %}.

כעת, לכל {% equation %}x\ne y{% endequation %} שניתנים להשוואה צריך להתקיים {% equation %}fg\left(x,y\right)=\epsilon\left(x,y\right)=0{% endequation %}, ולכן על פי הנוסחה {% equation %}\sum_{x\le z\le y}f\left(x,z\right)g\left(z,y\right)=0{% endequation %}. בואו נבודד מהסכום הזה את האיבר שמתקבל כש-{% equation %}z=x{% endequation %} ונעביר אגף, נקבל ש:

{% equation %}g\left(x,y\right)=-\left(f\left(x,x\right)\right)^{-1}\sum_{x&lt;z\le y}f\left(x,z\right)g\left(z,y\right){% endequation %}.

הנוסחה הזו מספיקה כדי <strong>להגדיר</strong> את {% equation %}g{% endequation %} לכל קטע באופן רקורסיבי. זה לא מבטיח לנו נוסחה פשוטה יותר עבור {% equation %}g{% endequation %}, ומכאן בפרט שאין לנו תמיד נוסחה פשוטה עבור {% equation %}\mu{% endequation %}. מה כן יש לנו? ובכן, אם נציב את {% equation %}\zeta{% endequation %} בתור {% equation %}f{% endequation %} בנוסחאות הללו, נקבל ש-{% equation %}\mu{% endequation %} מתוארת על ידי הנוסחאות הבאות:

{% equation %}\mu\left(x,x\right)=1{% endequation %} לכל {% equation %}x\in X{% endequation %}.

{% equation %}\mu\left(x,y\right)=-\sum_{x&lt;z\le y}\mu\left(z,y\right)=-\sum_{x\le z&lt;y}\mu\left(x,z\right){% endequation %} לכל {% equation %}x&lt;y{% endequation %}.

את נוסחת ההיפוך עצמה ניתן לתאר עם סכומים באופן הבא: אם {% equation %}f\zeta=g{% endequation %} זה אומר ש-{% equation %}g\left(x,y\right)=\sum_{x\le z\le y}f\left(x,z\right){% endequation %}, ולכן {% equation %}f\left(x,y\right)=\sum_{x\le z\le y}g\left(x,z\right)\mu\left(z,y\right){% endequation %}.

כזכור, נוסחת ההיפוך דיברה על פונקציות שמוגדרות לא על קטעים, אלא על איברים. היא אמרה שמתקיים

{% equation %}g\left(x\right)=\sum_{y\le x}f\left(y\right){% endequation %}

אם ורק אם

{% equation %}f\left(x\right)=\sum_{y\le x}g\left(y\right)\mu\left(y,x\right){% endequation %}

בניסוח הזה אנחנו חייבים שב-{% equation %}X{% endequation %} כל אידאל סדר ראשי יהיה סופי פשוט כי אחרת הסכום {% equation %}\sum_{y\le x}{% endequation %} (כאשר {% equation %}x{% endequation %} קבוע - כלומר, הסכום הוא בדיוק על איברי אידאל הסדר שנוצר על ידי {% equation %}x{% endequation %}) איננו סופי. למעשה, יש כאן נקודה עדינה למדי - אותן {% equation %}f,g{% endequation %} שאני מדבר עליהן כאן מוגדרות על איברים של {% equation %}X{% endequation %}, לא על קטעים. אין בעיה של ממש לטפל בעניין הזה אבל אני חושב שהתעללתי בקוראים מספיק ואסיים כאן.