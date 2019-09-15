---
id: 2580
title: "על P=NP מעל חבורות אבליות - מבוא שלם"
date: 2013-06-15 09:45:02
layout: post
categories: 
  - אלגברה מופשטת
  - לוגיקה
  - תורת הסיבוכיות
tags: 
  - חבורות אבליות
  - מודלים חישוביים
  - שאלת P=NP
---
בואו נוכיח ש-{% equation %}\mbox{P}\ne\mbox{NP}{% endequation %}.

אה... מה?

<a href="http://www.gadial.net/2010/08/15/p_vs_np_overview/">תיארתי בעבר בבלוג</a> את בעיית {% equation %}\mbox{P=NP}{% endequation %} בתור הבעיה הפתוחה המרכזית במדעי המחשב ולא הרבה השתנה מאז - עדיין אין לנו הוכחה ש-{% equation %}\mbox{P}\ne\mbox{NP}{% endequation %} למרות שרוב מדעני המחשב חושבים שזה המצב. אז מן הסתם לא על הבעיה הזו אני רוצה לדבר. אני רוצה לדבר על {% equation %}\mbox{P}\ne\mbox{NP}{% endequation %} מעל מודל חישוב <strong>אחר</strong>, אבל כזה שלדעתי לא שונה יותר מדי באופיו ממודל החישוב הרגיל (אם כי אחרים - למשל, אני - עשויים לחלוק עלי ולטעון שיש הבדלים מהותיים ביותר ושנראה אותם עוד בפוסט הזה). פורמלית מה שארצה להראות הוא שלכל <strong>חבורה אבלית אינסופית</strong> {% equation %}G{% endequation %} מתקיים {% equation %}\mbox{P}_{G}\ne\mbox{NP}_{G}{% endequation %} כאשר {% equation %}\mbox{P}_{G},\mbox{NP}_{G}{% endequation %} הן מחלקות הסיבוכיות הרלוונטיות מעל החבורה {% equation %}G{% endequation %}. כמובן שתכף אגדיר את הכל במפורש, אבל רק כדי שנהיה סגורים על האופן שבו התוצאה הזו מתקשרת לתורת הסיבוכיות הרגילה: במקרה שבו {% equation %}G=\mathbb{Z}_{2}{% endequation %} אנו מקבלים את המחלקות {% equation %}\mbox{P},\mbox{NP}{% endequation %} ה"רגילות".

ההוכחה שאציג תתבסס על המאמר של Prunescu שאפשר לראות <a href="http://home.mathematik.uni-freiburg.de/prunescu/grupshor.pdf">כאן</a>. זו הוכחה קצרצרה של ארבעה עמודים, אבל כזו שמסתמכת על לא מעט ידע מוקדם שאציג בפוסטים בצורה מקיפה יותר. זו אחת הסיבות לכך שזו תוצאה כל כך יפה: היא מערבת מושגים ורעיונות מתורת הסיבוכיות, תורת החבורות ותורת המודלים, ותיתן לנו הזדמנות להכיר כמה מושגים ותוצאות שטרם הוזכרו בבלוג ולראות איך משתמשים בהן בפועל.

נתחיל עם להסביר מה זה בכלל המודל החישובי הזה, "חישוב מעל חבורה {% equation %}G{% endequation %}". אני אנסה דווקא לא להיכנס להגדרות מדויקות פה אלא להסביר את הרעיון כפי שאני מבין אותו. אני מזהיר מראש שהבקיאות שלי בנושאים הללו היא לא משהו ולפעמים יכולה להיות תלות לא טריוויאלית של מחלקות הסיבוכיות בהגדרה המדויקת של המודל, כך שאני עלול לטעות; אתם מוזמנים לאתגר אותי בתגובות.

הרעיון הוא זה: קחו את שפת התכנות החביבה עליכם. אפשר להשתמש בה כמות שהיא - יש לנו משתנים שהם מספרים, מחרוזות, ערכים בוליאניים... הכל כרגיל. יש לכם גם את כל פונקציות הספריה שאתם מכירים ואוהבים והכל טוב ויפה. אלא שבנוסף לכך יש מחלקה בשם {% equation %}G{% endequation %} שאין לכם גישה להגדרות הפנימיות שלה. כל מה שיש לכם הוא קבוע {% equation %}e\in G{% endequation %}, ולמשתנים ששייכים למחלקה {% equation %}G{% endequation %} יש שלוש מתודות - האחת, {% equation %}={% endequation %}, מקבלת משתנה נוסף השייך למחלקה {% equation %}G{% endequation %} ומחזירה {% equation %}\mbox{True}{% endequation %} אם הם שווים ואחרת {% equation %}\mbox{False}{% endequation %}; השניה, {% equation %}+{% endequation %}, מקבלת משתנה נוסף השייך למחלקה {% equation %}G{% endequation %} ומחזירה את החיבור של שתיהן, על פי כלל החיבור בחבורה {% equation %}G{% endequation %}, ומובטח לנו ש-{% equation %}a+e=e+a=a{% endequation %} לכל {% equation %}a\in G{% endequation %}, והשלישית, {% equation %}-{% endequation %}, מקבלת משתנה אחד {% equation %}a{% endequation %} השייך למחלקה {% equation %}G{% endequation %} ומחזירה משתנה אחר {% equation %}-a{% endequation %}, כך שמובטח שמתקיים {% equation %}a+\left(-a\right)=e{% endequation %}. אין לכם יכולת לחבר איברים של {% equation %}G{% endequation %} עם משתנים מסוג אחר (למשל, עם מספרים שלמים) או להשוות אותם למספרים מסוג שונה; אברי {% equation %}G{% endequation %} הם סוג של "קופסה שחורה".

כל בעיה חישובית מהסוג שעליו נרצה לדבר כאן תהיה מהסוג הבא: אנחנו מקבלים כקלט מערך של משתנים מתוך {% equation %}G{% endequation %}, שאורכו ידוע רק בזמן ריצה (כלומר, אנחנו צריכים להתמודד עם מערך מאורך כלשהו) וצריכים להחזיר כפלט {% equation %}\mbox{True}{% endequation %} או {% equation %}\mbox{False}{% endequation %}, בהתאם לתכונה שהמערך הזה מקיים או לא מקיים. בואו נציג מייד דוגמה לבעיה כזו כדי שיהיה ברור - זו תהיה הבעיה המרכזית שנעסוק בה בפוסט. במאמר קוראים לה Nullsack (וריאציה על Knapsack, למי שמכיר).

{% equation %}\Sigma_{G}=\left\{ \left(x_{1},\dots,x_{n}\right)\in G^{n}\ |\ n\in\mathbb{N}\wedge\exists J\ne\emptyset:\sum_{i\in J}x_{i}=e\right\} {% endequation %}

מילולית, ב-{% equation %}\Sigma_{G}{% endequation %} כלולים כל הוקטורים מאורך {% equation %}n{% endequation %} טבעי <strong>כלשהו</strong> (כלומר, יכולים להיות שם וקטורים מאורך 1, מאורך 10, מאורך {% equation %}10^{100}{% endequation %} וכן הלאה) שאפשר לסכום <strong>חלק</strong> מהאיברים בהם ולקבל את {% equation %}e{% endequation %}. במקרה שבו {% equation %}G=\mathbb{Z}{% endequation %}, זו השאלה הבאה: נותנים לכם אוסף של מספרים שלמים (לא קבוצה במובן המתמטי, כי אותו מספר יכול להופיע כמה פעמים) - האם אפשר לבחור מתוכו תת-אוסף של מספרים שהסכום שלהם הוא 0?

הבעיה הזו היא בעיה מוכרת מאוד בתורת הסיבוכיות: היא נקראת Subset-Sum והיא דוגמה פשוטה ושימושית לבעייה חישובית שהיא NP-שלמה. אלא שיש הבדל קריטי שחייבים לתת עליו את הדעת מייד: במודל הרגיל של תורת הסיבוכיות (מכונת טיורינג "רגילה"), הקלט ל-Subset-Sum נתון בתור <strong>סדרה של ביטים</strong> שמקודדת את וקטור המספרים, וזמן הריצה של האלגוריתם נמדד <strong>ביחס לאורך סדרת הביטים</strong> הזו. לעומת זאת, במודל החדש שהצגתי, זמן החישוב נמדד תמיד ביחס למספר {% equation %}n{% endequation %} ותו לא, והקלט נתון לנו בתור "קופסה שחורה". ההבדל הזה הוא קריטי. אנסה לתת דוגמה: נניח שהחבורה שלנו {% equation %}G{% endequation %} היא אכן {% equation %}\mathbb{Z}{% endequation %}. אז אם האיבר {% equation %}a\in G{% endequation %} היה מיוצג בתור סדרת ביטים, היינו יכולים לחלק אותו ב-2 בקלות, על ידי הסרת הביט הימני ביותר ממנו. במודל החדש אין לי מושג איך אפשר לחלק את המספר ב-2. ונניח (רק לצורך ההמחשה) שאיכשהו יש לי משתנה מהמחלקה {% equation %}G{% endequation %} שידוע לי שמכיל את הערך {% equation %}1{% endequation %}, ויש לי משתנה אחר {% equation %}a{% endequation %} שידוע לי שהוא חזקה כלשהי של {% equation %}2{% endequation %} ואני רוצה "לגלות" מה הערך המספרי שלו. אז אפשר לחבר את 1 ל-1 ולקבל 2, ואת 2 ל-2 ולקבל 4, ואת 4 ל-4 ולקבל 8 וכך הלאה לקבל חזקות של {% equation %}2{% endequation %} ובכל פעם להשוות ל-{% equation %}a{% endequation %}. מספר הפעולות שיידרש לנו לעשות את זה הוא מאותו סדר גודל של מספר הביטים שנדרשים כדי לייצג את {% equation %}a{% endequation %}, דהיינו זה זמן ריצה <strong>לינארי</strong> בגודל הייצוג של {% equation %}a{% endequation %}, כלומר במודל הקלאסי, אבל זה זמן ריצה <strong>לא חסום</strong> ב<strong>מספר</strong> הקלטים שלנו, כלומר במודל ה"חדש". בכל מקרה, אני מקווה שכבר קיבלתם את התחושה שחישובים במודל החדש הם <strong>יותר קשים</strong> מאשר במודל הרגיל, בגלל שהקלט פחות נגיש לנו.

למי שעדיין לא הבין את ההבדלה הזו, לא נורא - בהמשך נראה בדיוק איך היא רלוונטית לנו.

עכשיו אפשר להגדיר את {% equation %}\mbox{P}_{G}{% endequation %}: אלו כל בעיות ההכרעה שניתן לפתור במודל החישובי מעל {% equation %}G{% endequation %} בזמן שהוא פולינומי באורך הקלט (כלומר, באורך של וקטור הקלטים שהתקבל). אבל עדיין צריך להגדיר את {% equation %}\mbox{NP}_{G}{% endequation %}. וכאן יש לנו דילמה כלשהי. בואו ניזכר שניה בהגדרה של {% equation %}\mbox{NP}{% endequation %} הרגילה: אנחנו אומרים ש-{% equation %}L\in\mbox{NP}{% endequation %} אם קיים אלגוריתם פולינומי {% equation %}M{% endequation %} שמקבל שני סוגי קלטים: הקלט ה"רגיל", שמסומן ב-{% equation %}x{% endequation %}, וקלט שהוא "עד", או "הוכחה" לשייכות של {% equation %}x{% endequation %} ל-{% equation %}M{% endequation %}, שמסומן {% equation %}y{% endequation %}. הפולינומיות של {% equation %}M{% endequation %} היא ביחס לגודל הייצוג של {% equation %}x{% endequation %}, וגם {% equation %}x{% endequation %} וגם {% equation %}y{% endequation %} הם סדרות של ביטים (מכאן יוצא שאפשר להניח שהגודל של {% equation %}y{% endequation %} יהיה גם הוא פולינומי בגודל הייצוג של {% equation %}x{% endequation %} כי אחרת {% equation %}M{% endequation %} ממילא לא הייתה מצליחה לקרוא את הכל ולעמוד במגבלות הזמן שלה). אנו דורשים שאם {% equation %}x\in L{% endequation %} אז יהיה {% equation %}y{% endequation %} כלשהו כך ש-{% equation %}M\left(x,y\right)=\mbox{True}{% endequation %}, אבל שאם {% equation %}x\notin L{% endequation %} אז לכל {% equation %}y{% endequation %} שהוא, {% equation %}M\left(x,y\right)=\mbox{False}{% endequation %}. למשל, ב-Subset-Sum ה-{% equation %}x{% endequation %} הוא וקטור של מספרים שלמים, ואילו {% equation %}y{% endequation %} הוא קבוצת האינדקסים {% equation %}J{% endequation %} שיש לסכום, במקרה שבו אכן קיימת קבוצה כזו.

הדילמה שעומדת בפנינו היא זו: בהינתן {% equation %}x{% endequation %} שהוא וקטור של אברי {% equation %}G{% endequation %}, מה יהיה {% equation %}y{% endequation %}? הוא יכול להיות וקטור של אברי {% equation %}G{% endequation %} בעצמו, והוא גם יכול להיות סתם וקטור של ביטים. די בבירור המקרה הראשון חזק יותר מהשני (כי וקטור ביטים ודאי שאפשר "לקודד" בעזרת וקטור של אברי {% equation %}G{% endequation %}: 0 יהיה {% equation %}e{% endequation %} ו-1 יהיה כל איבר שאינו {% equation %}e{% endequation %}) ולא ברור אוטומטית מה ההגדרה ה"נכונה". מכיוון שהתוצאה שאנחנו רוצים להראות היא ש-{% equation %}\mbox{P}_{G}\ne\mbox{NP}_{G}{% endequation %}, כלומר ש-{% equation %}\mbox{NP}_{G}{% endequation %} היא מחלקה <strong>גדולה יותר</strong>, הרי שאם נראה את זה עבור ההגדרה של "עד" שמקודד על ידי ביטים, בוודאי שהתוצאה תנבע גם עבור "עד" שמקודד על ידי אברי {% equation %}G{% endequation %}. לכן נשתמש בהגדרה-מבוססת-הביטים בפוסטים על הנושא.

שימו לב שבבירור Subset-Sum שייך ל-{% equation %}\mbox{NP}_{G}{% endequation %}: בהינתן וקטור {% equation %}x=\left(x_{1},\dots,x_{n}\right){% endequation %}, ה-{% equation %}y{% endequation %} שלנו יהיה סדרה של {% equation %}n{% endequation %} ביטים {% equation %}\left(b_{1},\dots,b_{n}\right){% endequation %} כך ש-{% equation %}\sum b_{i}x_{i}=e{% endequation %}. את החישוב קל מאוד לבצע, כמובן. לכן כל מה שנשאר לעשות הוא להשתכנע ש-Subset-Sum <strong>אינה</strong> שייכת ל-{% equation %}\mbox{P}_{G}{% endequation %}, כלומר ש<strong>אף</strong> אלגוריתם לא יוכל לפתור את הבעיה בזמן פולינומי. וכאן מן הסתם יהיה עיקר הסיבוך - איך אפשר לטעון טענה כל כך כללית, על <strong>כל</strong> אלגוריתם, מחוכם ומסובך ככל שיהיה?

הדרך לעשות דבר כזה היא לתקוף את האלגוריתם בדרך עקיפה - את האופן שבו האלגוריתם <strong>משיג מידע על הקלט</strong>. כאן אנחנו גם נפרדים לשלום מבעיית {% equation %}\mbox{P}=\mbox{NP}{% endequation %} הרגילה, שבה <strong>אי אפשר </strong>לעשות תעלולים כאלו בגלל שהאלגוריתמים הרלוונטיים יודעים (במובן מסויים) את "הכל" על הקלט (אבל גם בסיבוכיות "רגילה", בהקשרים של מחלקות סיבוכיות אחרות, דרך התקיפה הזו עובדת, כי מחלקות הסיבוכיות מגבילות איכשהו את היכולת לבדוק את כל הקלט, או לבצע עליו חישובים מסויימים, או לזכור אותו בשלמותו). מה שנרצה לעשות הוא להראות שיש שני קלטים <strong>שונים</strong> לאלגוריתם, אחד ששייך ל-Subset-Sum והשני שלא שייך ל-Subset-Sum, כך שבכל דרך אפשרית שבה האלגוריתם "דוגם" אותם הוא מקבל את אותו מידע בדיוק, ולכן מבחינתו שני הקלטים הללו נראים זהים, ולכן הוא יענה עליהן את אותן התשובה בדיוק, ובהכרח יטעה עבור אחד מהם.

נראה איך אפשר לעשות דבר כזה במקרה הפרטי שבו {% equation %}G=\mathbb{Z}{% endequation %}. אחר כך נראה איך עושים את זה עבור עוד מחלקה מעניינת של חבורות, ואז ננטוש את הסיבוכיות ונעבור לדבר על תורת המודלים ונשתמש בתעלול מתוכה כדי להראות שההוכחות שלנו יעבדו עבור כל חבורה. אבל לעת עתה, בואו נתמקד במקרה של {% equation %}G=\mathbb{Z}{% endequation %}. מה קורה כאן?

ובכן, האלגוריתם מקבל קלטים, {% equation %}\left(x_{1},\dots,x_{n}\right){% endequation %}. הוא יכול לבצע עליהם פעולות חיבור וחיסור ולקבל איברים חדשים שהם <strong>צירופים לינאריים</strong> של {% equation %}\left(x_{1},\dots x_{n}\right){% endequation %} עם מקדמים מתוך {% equation %}\mathbb{Z}{% endequation %}. כלומר, איבר כללי ב-{% equation %}G{% endequation %} שהמשתמש יכול לבנות הוא מהצורה {% equation %}\sum_{i=1}^{n}a_{i}x_{i}{% endequation %} כך ש-{% equation %}a_{i}\in\mathbb{Z}{% endequation %} (האלגוריתם גם יכול לחבר או לחסר את {% equation %}e{% endequation %} לכל זה, אבל זה לא ישפיע על ערך הסכום ולכן לא צריך להתייחס לזה).

חישובים זה טוב ויפה, אבל מה שמשפיע על ריצת האלגוריתם בסופו של דבר הם ערכים בוליאנים - זה מה שמשפיע על התפצלויות בתוכנית ועל לולאות. הדרך היחידה להפיק ערכים בוליאנים מתוך איברי {% equation %}G{% endequation %} היא באמצעות פונקציית ה-{% equation %}={% endequation %}. על שני איברים כלליים, החישוב יבדוק אם {% equation %}\sum_{i=1}^{n}a_{i}x_{i}=\sum_{i=1}^{n}b_{i}x_{i}{% endequation %}, כאשר {% equation %}a_{i},b_{i}\in\mathbb{Z}{% endequation %}. אפשר לפשט את זה - הבדיקה הזו שקולה לבדיקה האם {% equation %}\sum_{i=1}^{n}\left(a_{i}-b_{i}\right)x_{i}=0{% endequation %}, או בסימון אחר - האם {% equation %}\sum_{i=1}^{n}c_{i}x_{i}=0{% endequation %} כאשר {% equation %}c_{i}\in\mathbb{Z}{% endequation %}. בסימון עוד יותר קומפקטי: האם {% equation %}c\cdot x=0{% endequation %}, כאשר {% equation %}c{% endequation %} ו-{% equation %}x{% endequation %} שניהם וקטורים והמכפלה היא מכפלה סקלרית "רגילה".

בואו ניקח עכשיו אלגוריתם פולינומי קונקרטי ונחסל אותו. נשחק איתו את המשחק הבא: נתחיל להריץ אותו וניתן לו לעשות איזה חישובים שבא לו, אבל בכל פעם שהוא בודק שוויון בין שני איברים של {% equation %}G{% endequation %} נענה לו "לא", אלא אם זה שוויון טריוויאלי לחלוטין - כזה שבו במשוואה {% equation %}\sum_{i=1}^{n}c_{i}x_{i}=0{% endequation %} המתאימה כל ה-{% equation %}c_{i}{% endequation %}-ים הם 0 (למשל, אם הוא שואל האם {% equation %}x_{1}=x_{1}{% endequation %}). האלגוריתם ירוץ ירוץ ירוץ ירוץ וישאל שאלות, אבל בסופו של דבר הוא חייב לעצור ולענות "כן" או "לא", הרי הוא בעל זמן ריצה פולינומי ובפרט חסום.

עכשיו נוכל לפרוש את כל השאלות הלא טריוויאליות שהאלגוריתם שאל במהלך הריצה:

{% equation %}c^{1}\cdot x\ne0{% endequation %}

{% equation %}c^{2}\cdot x\ne0{% endequation %}

{% equation %}\vdots{% endequation %}

{% equation %}c^{m}\cdot x\ne0{% endequation %}

סה"כ {% equation %}m{% endequation %} שאלות, כאשר {% equation %}m{% endequation %} פולינומי ב-{% equation %}n{% endequation %} ({% equation %}n{% endequation %} הוא מספר האיברים ב-{% equation %}x{% endequation %}, כזכור). כעת אנחנו חושבים על {% equation %}x{% endequation %} בתור וקטור של <strong>משתנים</strong> שהם מספרים שלמים, ועל השאלות של האלגוריתם בתור <strong>אי שוויונים</strong>, ואנחנו שואלים את עצמנו אם קיימת הצבת ערכים אפשרית ל-{% equation %}x{% endequation %} שתספק את כל האי-שוויונים בו זמנית. יותר מכך - אנחנו רוצים <strong>שני</strong> פתרונות, {% equation %}x,y{% endequation %} לאותה מערכת משוואות, אבל כך ש-{% equation %}x{% endequation %} שייך ל-Subset-Sum ואילו {% equation %}y{% endequation %} לא שייך. אם נוכיח שקיימים שני וקטורים כאלו, הרי שהוכחנו שהאלגוריתם טועה על אחד מהם, ובכך חיסלנו אותו. להוכיח פורמלית שקיימים שני פתרונות כאלו זה קצת טכני ולא אכנס לזה (היי, גם המאמר לא!) אבל אפשר להבין את הרעיון לא רע אם חושבים על הסיטואציה בדו-מימד, כלומר כאשר {% equation %}n=2{% endequation %}: נוח לעבור לדבר על גיאומטריה ולכן אפשר לדבר על המרחב הוקטורי {% equation %}\mathbb{Q}^{2}{% endequation %} (כל הנקודות הרציונליות במישור), ואז כל משוואה מהצורה {% equation %}c\cdot x=0{% endequation %} מגדיר <strong>ישר</strong> במרחב הזה. הפואנטה כעת היא שאיחוד סופי של ישרים לא יכול לכסות את כל המישור; השאלה אם נקודה במישור תכוסה על ידי אחד מהישרים זהה לשאלה אם היחס בין הקואורדינטות שלה שווה לשיפוע של אחד הישרים בקבוצה, אבל קבוצת השיפועים הזו סופית ויש אינסוף שיפועים אפשריים. זה מבטיח שאפשר למצוא פתרון למערכת האי-שוויונים ב-{% equation %}\mathbb{Q}^{2}{% endequation %}, ואפשר לעבור ממנו ל-{% equation %}\mathbb{Z}^{2}{% endequation %} על ידי לקיחת הפתרון וכפל במכנה המשותף של הגורמים בו. שימו לב שבלי האינסופיות של {% equation %}\mathbb{Z}{% endequation %} זה לא היה עובד.

האתגר הוא לוודא שאחד הפתרונות שייך ל-Subset-Sum. באופן כללי לא בטוח שנוכל למצוא פתרון כזה! למשל, נניח שלכל וקטור ב-{% equation %}\left\{ 0,1\right\} ^{n}{% endequation %} שאינו וקטור האפס, יש שאלה {% equation %}c^{i}{% endequation %} כלשהי שהאלגוריתם שאל ששווה לוקטור הזה (כלומר, האלגוריתם ביצע "חיפוש ממצה") - ברור שלא נוכל למצוא פתרון {% equation %}x{% endequation %} שמצד אחד עונה "לא שווה לאפס" על כל {% equation %}c^{i}\cdot x{% endequation %} ומצד שני כן עונה {% equation %}a\cdot x=0{% endequation %} על {% equation %}a\in\left\{ 0,1\right\} ^{n}{% endequation %} כלשהו.

כאן אנחנו חייבים להשתמש בכך שהאלגוריתם הוא <strong>פולינומי</strong> (שהרי כל מטרתו היא להוכיח ש-Subset-Sum שייכת ל-{% equation %}\mbox{P}_{\mathbb{Z}}{% endequation %}. זה אומר שקיים {% equation %}n{% endequation %} גדול דיו כך שזמן הריצה הכולל של האלגוריתם יהיה לכל היותר {% equation %}2^{n}-2{% endequation %} צעדים, כלומר בפרט {% equation %}m&lt;2^{n}-1{% endequation %}. זה מבטיח (שוב, נדרשת פה קצת עבודה טכנית) שיהיה {% equation %}a\in\left\{ 0,1\right\} ^{n}{% endequation %} שלא "מכוסה" על ידי אף אחת מהשאלות של האלגוריתם, ולכן אפשר למצוא {% equation %}x{% endequation %} כך ש-{% equation %}c^{i}\cdot x\ne0{% endequation %} לכל {% equation %}i{% endequation %} אבל {% equation %}a\cdot x=0{% endequation %}.

זה מסיים את ההוכחה במקרה שבו אנחנו מעל החבורה הקונקרטית {% equation %}\mathbb{Z}{% endequation %}. למי שמתעניין בתורת הסיבוכיות נטו, הסיפור נגמר כאן: טכניקת ההוכחה שראינו היא כל מה שהולך להיות כאן בכל הנוגע לתורת הסיבוכיות; ההמשך, שבו אנחנו מנסים להכליל את התוצאה לכל חבורה {% equation %}G{% endequation %} יתבסס בעיקר על אבחנות מתוך תורת החבורות ותורת המודלים שיאפשרו לנו להשתמש "בחינם" בטכניקה שכבר ראינו. יהיה אקשן.