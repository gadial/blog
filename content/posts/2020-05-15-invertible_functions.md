---
title: "תורת הקבוצות - פונקציות חד-חד-ערכיות, על והפיכות"
layout: post
categories:
  - תורת הקבוצות
tags:
  - תורת הקבוצות
  - פונקציות
---

בסדרת הפוסטים שלי על תורת הקבוצות סיימתי להגדיר מהן פונקציות, ועכשיו אני רוצה להראות את שתי התכונות החשובות ביותר שמדברים עליהן בהקשר של פונקציות: פונקציות <strong>חד-חד-ערכיות</strong> ופונקציות <strong>על</strong>. שתי התכונות הללו הן לא משהו אקראי שנבחר להיות מעניין בצורה שרירותית - חיש קל נראה שהן מגיעות הישר מלב ההגדרה של מהי פונקציה בכלל.

ראשית, בואו נגדיר את שתי התכונות הללו. ניקח פונקציה {% equation %}f:A\to B{% endequation %}. אינטואיטיבית - זה משהו שלוקח קלט מתוך {% equation %}A{% endequation %} ומחזיר פלט מתוך {% equation %}B{% endequation %}. כעת, התכונה "{% equation %}f{% endequation %} חד-חד-ערכית" פירושה ש<strong>קלטים שונים מחזירים פלטים שונים</strong> או במילים אחרות, <strong>אין שני קלטים שונים שנותנים את אותו פלט</strong>. פורמלית: אם {% equation %}a_{1}\ne a_{2}\in A{% endequation %} אז {% equation %}f\left(a_{1}\right)\ne f\left(a_{2}\right){% endequation %}, או בניסוח אחר, שימושי אולי אפילו יותר: אם {% equation %}f\left(a_{1}\right)=f\left(a_{2}\right){% endequation %} אז {% equation %}a_{1}=a_{2}{% endequation %}.

הנה דוגמא פשוטה: אם נגדיר פונקציה מכל המכוניות שכרגע על הכביש אל מספר הרישוי שלהן, הפונקציה הזו תהיה חד-חד-ערכית כי אין שני רכבים עם אותו מספר רישוי (אני מאוד מקווה!). אם נגדיר פונקציה מכל המכוניות הללו אל <strong>הצבע</strong> שלהן, היא תהיה מאוד לא חד-חד-ערכית; זה ניחוש סביר שיהיו על הכביש שתי מכוניות שונות בצבע לבן.

בואו נראה דוגמאות מקרב הפונקציות הממשיות, {% equation %}f:\mathbb{R}\to\mathbb{R}{% endequation %}. הפונקציה {% equation %}f\left(x\right)=x{% endequation %} היא חד-חד-ערכית, באופן די מובן מאליו כי אם {% equation %}f\left(a_{1}\right)=f\left(a_{2}\right){% endequation %} אז מההגדרה של {% equation %}f{% endequation %} נקבל {% equation %}a_{1}=f\left(a_{1}\right)=f\left(a_{2}\right)=a_{2}{% endequation %}. הנה משהו קצת יותר מחוכם: הפונקציה הלינארית {% equation %}f\left(x\right)=3x-7{% endequation %} היא חד-חד-ערכית כי אם {% equation %}f\left(a_{1}\right)=f\left(a_{2}\right){% endequation %} אז {% equation %}3a_{1}-7=3a_{2}-7{% endequation %} ואם נחבר 7 לשני האגפים ונחלק ב-3 נקבל {% equation %}a_{1}=a_{2}{% endequation %}.

לעומת זאת הפונקציה {% equation %}f\left(x\right)=x^{2}{% endequation %} <strong>איננה </strong>חד-חד-ערכית כי {% equation %}f\left(1\right)=f\left(-1\right)=1{% endequation %}. מה השתבש? למה אי אפשר להגיד {% equation %}a_{1}^{2}=a_{2}^{2}{% endequation %} ואז להוציא שורש משני האגפים? בדיוק בגלל שפעולת הוצאת השורש דורשת מאיתנו <strong>לאבד מידע</strong>. אם תזכרו, בפוסט הקודם אמרתי משהו על כך שהוצאת שורש היא משהו מוזר שנקרא <strong>פונקציה רב ערכית</strong> ומה שאנחנו עובדים איתו בדרך כלל הוא רק <strong>ענף</strong> של הפונקציה. לא חייבים להיכנס לדקות הזו; רק להיות מודעים לכך שלא כל פעולה שאנחנו מפעילים על שני אגפי משוואה מבטיחה שפתרונות אפשריים לא ילכו לאיבוד.

באופן שאולי קצת מפתיע, {% equation %}f\left(x\right)=x^{3}{% endequation %} היא דווקא <strong>כן</strong> פונקציה חד-חד-ערכית כשמדובר על פונקציה במספרים ממשיים; זאת מכיוון של-{% equation %}a^{3}{% endequation %} יש <strong>שלושה</strong> שורשים אפשריים ש-{% equation %}a{% endequation %} הוא רק אחד מהם, אבל שני השורשים האחרים הם מספרים מרוכבים <strong>שאינם ממשיים</strong>. אם כן, השאלה מתי פונקציה היא חד-חד-ערכית או לא עשויה להיות טריקית למדי; צריך להיזהר עם זה.

בשביל האינטואיציה שלנו, הנה קריטריון פשוט שמאפשר "לראות" מתי פונקציה ממשית היא חד-חד-ערכית. נסתכל על הגרף שלה ונשאל את עצמנו את השאלה הבאה: האם קיים קו <strong>אופקי</strong> שחותך את גרף הפונקציה בשתי נקודות או יותר? שתי נקודות חיתוך כאלו שהן באותו גובה הן זוגות {% equation %}\left(x_{1},y\right),\left(x_{2},y\right){% endequation %} - כלומר שני קלטים של הפונקציה שנותנים את אותו פלט. אם מסתכלים על הגרף של {% equation %}f\left(x\right)=x^{2}{% endequation %} ("פרבולה מחייכת") רואים בקלות שהיא לא חד-חד-ערכית כי כל קו שגבוה מ-{% equation %}y=0{% endequation %} חותך אותה בשני מקומות; לעומת זאת הגרף של {% equation %}f\left(x\right)=x^{3}{% endequation %} ("אין לי מושג איך לקרוא לזה אבל זה פיתול מוזר שכזה") מקיים את תכונת החיתוך הזו יפה.

<img src="{{site.baseurl}}{{site.post_images}}/2020/04/graphs.PNG" alt=""/>

נעבור לתכונה השניה. פונקציה {% equation %}f:A\to B{% endequation %} היא <strong>על</strong> {% equation %}B{% endequation %} אם לכל פלט אפשרי אכן קיים קלט שמחזיר אותו: כלומר, לכל {% equation %}b\in B{% endequation %} קיים {% equation %}a\in A{% endequation %} כך ש-{% equation %}f\left(a\right)=b{% endequation %}. למשל, אם לכל מילה בשפה העברית {% equation %}f{% endequation %} מתאימה את האות הראשונה שלה, אז זו פונקציה על כי לכל אות בעברית קיימת מילה אחת לפחות שמתחילה באות הזו. לעומת זאת, הפונקציה שמחזירה לכל אדם בישראל את מספר תעודת הזהות שלו איננה על כי קיימים מספרים שאינם מספרי תעודת זהות. אבל רגע, הניסוח שלי קצת בעייתי - לא אמרתי <strong>על</strong> מה הפונקציה הזו אמורה להיות. האם על קבוצת <strong>כל</strong> המספרים הטבעיים? או אולי רק המספרים הטבעיים בני 9 ספרות בדיוק? או אולי הקבוצה "כל המספרים הטבעיים שהם מספר זהות של מישהו", מה שיגרום לפונקציה כן להיות על?

בואו נחזור אל שתי הפונקציות החביבות {% equation %}f\left(x\right)=x^{2}{% endequation %} ו-{% equation %}f\left(x\right)=x^{3}{% endequation %} ונשאל את עצמנו - האם הן על? אם חושבים עליהן בתור פונקציות {% equation %}f:\mathbb{R}\to\mathbb{R}{% endequation %}, אז {% equation %}f\left(x\right)=x^{2}{% endequation %} בוודאי איננה על, כי {% equation %}-1{% endequation %} אינו הפלט של אף קלט. לעומת זאת {% equation %}f\left(x\right)=x^{3}{% endequation %} היא כן על. אפשר לראות את זה בתמונה: פונקציה היא על אם כל קו אופקי חותך אותה <strong>לפחות פעם אחת</strong>.

על פניו, נראה שאם פונקציה אינה על קל "לתקן" את זה - פשוט נצמצם את הטווח שלה. למשל, עבור {% equation %}f\left(x\right)=x^{2}{% endequation %} אם נסתכל עליה בתור פונקציה {% equation %}f:\mathbb{R}\to[0,\infty({% endequation %} אז היא בהחלט פונקציה על. אבל מה זה אומר, לצמצם את הטווח? זה אומר להחליף את הפונקציה שלנו בפונקציה אחרת, שה"כלל" שמגדיר אותה זהה. זה אומר שעברנו לסיטואציה אחרת, שהיא אולי מועילה יותר בהקשר הנוכחי שלנו אבל לפעמים היא לא מועילה בכלל, ואני מקווה שזה יתברר בקרוב מעצמו. עדיין, כדאי לדבר במפורש על ה"תיקון" הזה: אם {% equation %}f:A\to B{% endequation %} היא פונקציה כלשהי, <strong>התמונה</strong> של {% equation %}f{% endequation %} על {% equation %}A{% endequation %} היא הקבוצה {% equation %}f\left(A\right)\triangleq\left\{ f\left(a\right)\ |\ a\in A\right\} {% endequation %} - זה אוסף האיברים ב-{% equation %}B{% endequation %} שמתקבלים בעזרת {% equation %}f{% endequation %}. עכשיו, אפשר תמיד לומר ש-{% equation %}f:A\to f\left(A\right){% endequation %} היא על; ואפשר גם לומר שהתכונה "להיות על" היא פשוט הטענה {% equation %}B=f\left(A\right){% endequation %}.

אפשר באופן דומה גם "לתקן" פונקציה שאיננה חח"ע על ידי צמצום של <strong>התחום</strong> שלה (כלומר, של {% equation %}A{% endequation %}): בכל פעם שיש לנו זוג של איברים של {% equation %}A{% endequation %} שמתמפים לאותו פלט, פשוט להעיף אחד מהם מתוך {% equation %}A{% endequation %}. לא הכי אלגנטי בעולם, אבל שימושי בהקשרים מסויימים.

עכשיו, אחרי שראינו קצת את התכונות הללו, בואו ונראה מאיפה הן מגיעות. ראשית, בואו נזכיר את שתי התכונות ש<strong>מגדירות</strong> מה זו פונקציה. יחס {% equation %}f\subseteq A\times B{% endequation %} הוא <strong>פונקציה</strong> אם מתקיים:

<ol> <li>"קיום": לכל {% equation %}a\in A{% endequation %} קיים {% equation %}b\in B{% endequation %} כך ש-{% equation %}\left(a,b\right)\in f{% endequation %}.</li>


<li>"יחידות": אם {% equation %}\left(a,b_{1}\right)\in f{% endequation %} וגם {% equation %}\left(a,b_{2}\right)\in f{% endequation %} עבור {% equation %}a\in A{% endequation %} ו-{% equation %}b_{1},b_{2}\in B{% endequation %} אז {% equation %}b_{1}=b_{2}{% endequation %}.</li>

</ol>

עכשיו אני אנסח את תכונות ה"על" וה"חד-חד-ערכית" באמצעות יחסים:

<ol> <li>"על": לכל {% equation %}b\in B{% endequation %} קיים {% equation %}a\in A{% endequation %} כך ש-{% equation %}\left(a,b\right)\in f{% endequation %}</li>


<li>"חד-חד-ערכית": אם {% equation %}\left(a_{1},b\right)\in f{% endequation %} וגם {% equation %}\left(a_{2},b\right)\in f{% endequation %} עבור {% equation %}a_{1},a_{2}\in A{% endequation %} ו-{% equation %}b\in B{% endequation %} אז {% equation %}a_{1}=a_{2}{% endequation %}.</li>

</ol>

הדמיון בין תכונות הקיום/יחידות ותכונות העל/חח"ע בולט מאוד, כמובן. נראה שההגדרות כמעט זהות עד כדי החלפת תפקידים בין {% equation %}A{% endequation %} ו-{% equation %}B{% endequation %}. ויש דרך לחדד את הדמיון עוד יותר אם <strong>נהפוך</strong> את {% equation %}f{% endequation %}. בואו נדבר על זה שניה.

{% equation %}f{% endequation %} היא פונקציה, ומעבר למשמעות האינטואיטיבית של "משהו שהופך קלט לפלט" פונקציה היא קודם כל <strong>יחס</strong> - אוסף של זוגות סדורים. אפשר פשוט לקחת כל זוג כזה ולהפוך את הסדר בין האיברים שלו, והתוצאה נקראת <strong>היחס ההפוך</strong>. פורמלית, אם {% equation %}R\subseteq A\times B{% endequation %} הוא יחס כלשהו, מגדירים {% equation %}R^{-1}\triangleq\left\{ \left(b,a\right)\ |\ \left(a,b\right)\in R\right\} {% endequation %}. עכשיו עבור המקרה הפרטי של פונקציה {% equation %}f{% endequation %} אפשר לעשות את אותו הדבר בדיוק: להגדיר {% equation %}f^{-1}\triangleq\left\{ \left(b,a\right)\ |\ \left(a,b\right)\in f\right\} {% endequation %}, ובסימון קצת יותר "פונקצייתי": {% equation %}f^{-1}\triangleq\left\{ \left(b,a\right)\ |\ f\left(a\right)=b\right\} {% endequation %}.

מתי {% equation %}f^{-1}{% endequation %} היא פונקציה? שימו לב לכך שהיחס {% equation %}f^{-1}{% endequation %} <strong>תמיד קיים</strong> אבל בהחלט <strong>לא</strong> מובטח שהוא יהיה פונקציה; פונקציה היא יחס שמקיים שני תנאים ספציפיים, "קיום" ו"יחידות", שפירושם עבור היחס {% equation %}f^{-1}\subseteq B\times A{% endequation %} הוא

<ol> <li>"קיום": לכל {% equation %}b\in B{% endequation %} קיים {% equation %}a\in A{% endequation %} כך ש-{% equation %}\left(b,a\right)\in f^{-1}{% endequation %}.</li>


<li>"יחידות": אם {% equation %}\left(b,a_{1}\right)\in f^{-1}{% endequation %} וגם {% equation %}\left(b,a_{2}\right)\in f^{-1}{% endequation %} עבור {% equation %}a_{1},a_{2}\in A{% endequation %} ו-{% equation %}b\in B{% endequation %} אז {% equation %}a_{1}=a_{2}{% endequation %}.</li>

</ol>

עכשיו, במקום לכתוב {% equation %}\left(b,a\right)\in f^{-1}{% endequation %} אני יכול לכתוב {% equation %}\left(a,b\right)\in f{% endequation %}: זו בדיוק ההגדרה של {% equation %}f^{-1}{% endequation %}. וכעת שתי השורות למעלה הופכות להיות:

<ol> <li>"קיום": לכל {% equation %}b\in B{% endequation %} קיים {% equation %}a\in A{% endequation %} כך ש-{% equation %}\left(a,b\right)\in f{% endequation %}.</li>


<li>"יחידות": אם {% equation %}\left(a_{1},b\right)\in f{% endequation %} וגם {% equation %}\left(a_{2},b\right)\in f{% endequation %} עבור {% equation %}a_{1},a_{2}\in A{% endequation %} ו-{% equation %}b\in B{% endequation %} אז {% equation %}a_{1}=a_{2}{% endequation %}.</li>

</ol>

ואלו בדיוק, אבל בדיוק, התכונות של "על" ו"חד-חד-ערכיות" של {% equation %}f{% endequation %}. אז אפשר לסכם את מה שראינו במשפט אחד קצר וקולע: {% equation %}f{% endequation %} היא חח"ע ועל אם ורק אם {% equation %}f^{-1}{% endequation %} היא פונקציה. במקרה הזה נהוג להגיד ש-{% equation %}f{% endequation %} היא <strong>הפיכה</strong>. למה? כי אפשר לחשוב על {% equation %}f^{-1}{% endequation %} בתור "אותה הפונקציה כמו {% equation %}f{% endequation %} רק בכיוון ההפוך". אם יש לנו {% equation %}a\in A{% endequation %} ואנחנו מפעילים את {% equation %}f{% endequation %} על {% equation %}a{% endequation %} ומקבלים {% equation %}f\left(a\right)=b{% endequation %} ואז מפעילים את {% equation %}f^{-1}{% endequation %} על {% equation %}b{% endequation %} אנחנו מקבלים {% equation %}f^{-1}\left(b\right)=a{% endequation %}, כלומר {% equation %}f^{-1}\left(f\left(a\right)\right)=a{% endequation %} - הפונקציה {% equation %}f^{-1}{% endequation %} "ביטלה" את הפעולה של {% equation %}f{% endequation %}.

פונקציות הפיכות הן כלי מרכזי בתורת הקבוצות - עליהן מתבססת ההגדרה שלנו ל<strong>שוויון עוצמות</strong> של קבוצות, שבאה לתת גישה אפשרית אחת לשאלה מתי שתי קבוצות (גם אינסופיות) הן מאותו גודל (ההגדרה פשוטה: {% equation %}A{% endequation %} שוות עוצמה ל-{% equation %}B{% endequation %} אם קיימת {% equation %}f:A\to B{% endequation %} הפיכה). נדבר על זה עוד בהמשך, אבל לפני כן אני ארצה לתת גישה מסודרת יותר לעניין ה"מפעילים את {% equation %}f{% endequation %} על קלט ואז מפעילים משהו אחר על הפלט" - זה יוביל אותנו למושג ה<strong>הרכבה</strong> שעליו אדבר בפוסט הבא. 