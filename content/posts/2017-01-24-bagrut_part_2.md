---
id: 3404
title: "בואו נפתור את הבגרות במתמטיקה! (חלק ב')"
date: 2017-01-24 13:12:46
layout: post
categories: 
  - כללי
tags: 
  - בגרות
  - מתמטיקה תיכונית
---
אני ממשיך את מה שעשיתי <a href="http://www.gadial.net/2016/12/28/bagrut_part_1/">בפוסט הקודם</a> - פותר בחינת בגרות במתמטיקה, והפעם את חלק ב' שלה. והפעם, כבונוס, אני מתאר שתי טעויות מביכות במיוחד שהיו לי בפתרונות ולא שמתי לב אליהן בזמן אמת!

הבגרות היא שאלון 317 של קיץ 2016.
<h1>שאלה 1</h1>
<a href="{{site.baseurl}}{{site.post_images}}/2017/01/2-question1.png" rel="attachment wp-att-3405"><img class="aligncenter size-full wp-image-3405" src="{{site.baseurl}}{{site.post_images}}/2017/01/2-question1.png" alt="2-question1" width="825" height="490" /></a>

אה, גאומטריה אנליטית. זה הולך להיות מעניין. מצד אחד, זה תחום חשוב ומועיל ואהבתי אותו בבית הספר ואני גם סוג של משתמש בו פה ושם בימינו. מצד שני, אני בטוח שאני לא שולט בכל מה שצריך בשביל לפתור מבחן בבית הספר (מעולם לא למדתי אליפסות, למשל). בואו נראה איך אסתדר.
<h1>סעיף א</h1>
יש לי בעיה כבר ברמת הטקסט הבסיסי: אין לי מושג מה זה "מדריך הפרבולה", אז אין לי מושג איך מוצאים את נקודת החיתוך שלו עם ציר {% equation %}x{% endequation %}. אז אני מגגל ונזכר בהגדרות: פרבולה עם משוואה {% equation %}y^{2}=2px{% endequation %} היא אוסף הנקודות שהמרחק שלהן מקו אנכי שנקרא "מדריך הפרבולה" ומנקודה על ציר {% equation %}x{% endequation %} ("מוקד הפרבולה") שווים. ה-{% equation %}p{% endequation %} שבנוסחת הפרבולה הוא המרחק בין המדריך והמוקד, והרעיון הוא שהפרבולה עוברת בראשית הצירים וברביעים 1 ו-4, כלומר המוקד נמצא ב-{% equation %}\frac{p}{2}{% endequation %} ואילו המדריך עובר דרך {% equation %}-\frac{p}{2}{% endequation %} ולכן המשוואה שלו היא {% equation %}x=-\frac{p}{2}{% endequation %}. במילים אחרות, {% equation %}A=\left(-\frac{p}{2},0\right){% endequation %}.

עכשיו, איך אני מוצא משיק לפרבולה בנקודה כלשהי? בטח נתנו נוסחה של זה בדף הנוסחאות, אבל למה שלא אנסה להמציא מחדש בעצמי. שיפוע המשיק לפונקציה כלשהי בנקודה מסויימת הוא הנגזרת של הפונקציה באותה נקודה. כאן יש לנו פרבולה שהיא לא בדיוק פונקציה אלא הדבקה של שתי פונקציות: {% equation %}y=\sqrt{2px}{% endequation %} ו-{% equation %}y=-\sqrt{2px}{% endequation %}. אפשר לגזור אותן וכאלה, אבל אני מכיר רמאות טכנית - אפשר גם לגזור את {% equation %}y^{2}=2px{% endequation %} בצורה סתומה, ומקבלים {% equation %}2y\cdot y^{\prime}=2p{% endequation %}, כלומר {% equation %}y^{\prime}=\frac{p}{y}{% endequation %}. אפשר להציב במקום {% equation %}y{% endequation %} את {% equation %}\pm\sqrt{2px}{% endequation %} אבל אני חושד שכרגע עם {% equation %}y{% endequation %} זה יהיה יותר מועיל לי. על טריקים כמו הגזירה הסתומה הזו אני אומר - ילדים, אל תנסו את זה בבית! יש הסבר מלא לתעלול הזה ויש לי <a href="http://www.gadial.net/2015/10/29/inverse_and_implicit_function/">פוסט בבלוג</a> עליו, אבל זה לא נושא שקל להבין.

עכשיו, נניח שיש לנו ישר שעובר דרך {% equation %}\left(x_{0},y_{0}\right){% endequation %} וגם דרך {% equation %}A=\left(-\frac{p}{2},0\right){% endequation %}. מה השיפוע שלו? באופן כללי השיפוע של ישר שעובר דרך {% equation %}\left(x_{1},y_{1}\right){% endequation %}ו-{% equation %}\left(x_{2},y_{2}\right){% endequation %} הוא {% equation %}m=\frac{y_{2}-y_{1}}{x_{2}-x_{1}}{% endequation %}, ולכן כאן הוא יהיה {% equation %}m=\frac{y_{0}}{x_{0}+\frac{p}{2}}{% endequation %}. יש לנו כבר ביטוי אחר לשיפוע שקיבלנו מתוך הגזירה של הפרבולה: {% equation %}m=\frac{p}{y_{0}}{% endequation %}. נשווה את שני אלו ונקבל:

{% equation %}\frac{p}{y_{0}}=\frac{y_{0}}{x_{0}+\frac{p}{2}}{% endequation %}

כלומר:

{% equation %}y_{0}^{2}=p\left(x_{0}+\frac{p}{2}\right){% endequation %}

עכשיו, אנחנו יודעים ש-{% equation %}y_{0}^{2}=2px_{0}{% endequation %}, כלומר קיבלנו:

{% equation %}2px_{0}=p\left(x_{0}+\frac{p}{2}\right){% endequation %}

ועל כן:

{% equation %}2px_{0}-px_{0}=\frac{p^{2}}{2}{% endequation %}

כלומר

{% equation %}x_{0}=\frac{p}{2}{% endequation %}

הגענו לשוויון הזה מתוך משוואה שההנחות היחידות שלה היו שהישר שלנו משיק לפרבולה ועובר דרך {% equation %}A{% endequation %}. ההנחות הללו הכריחו את קואורדינטת ה-{% equation %}x{% endequation %} של נקודת ההשקה להיות {% equation %}\frac{p}{2}{% endequation %}, וזה מסיים את הדבר הראשון שהיה צריך להראות.

הדבר השני, כרגיל בבגרות, לא באמת נכון בלי הנחה נוספת שהיא אולטרה-קטנונית - ששתי נקודות ההשקה לפרבולות שונות, כלומר שהמשיקים שונים זה מזה. מן הסתם אני מניח את זה בלי להניד עפעף. מה זה אומר? זה אומר שנקודות ההשקה חייבות לקיים {% equation %}y_{0}=\sqrt{2px_{0}}=p{% endequation %} עבור אחת מהן, ו-{% equation %}y_{0}=-\sqrt{2px_{0}}=-p{% endequation %} עבור השניה. זה ישפיע על השיפועים של המשיקים הללו. כדי לראות שהם מאונכים זה לזה, צריך לכפול את השיפועים ולראות שהם שווים {% equation %}-1{% endequation %}. רגע, מאיפה אני יודע את זה בכלל? נראה לי שזה זכרון עמום מימי התיכון שלי. למה שזה יהיה נכון? ובכן, מה זה "שיפוע" אצלנו? זה טנגנס הזווית שהישר יוצר עם ציר ה-{% equation %}x{% endequation %} (את זה קל לי לזכור כי אני זוכר שב-{% equation %}90^{\circ}{% endequation %} השיפוע הוא "אינסוף"). גיגול זריז נותן לי את הנוסחה למכפלת טנגנסים וקל לראות בה שאם ההפרש בין שתי זוויות הוא {% equation %}90^{\circ}{% endequation %} אז מכפלת הטנגנסים תצא מינוס 1 (אלא אם השיפוע הוא "אינסוף") - לא אלאה אתכם בזה, ממילא זו אקסיומה שכזו בתיכון. בקיצור, אני רוצה לבדוק את ערך המכפלה {% equation %}\frac{p}{p}\cdot\frac{p}{-p}{% endequation %} שכמובן שווה {% equation %}-1{% endequation %}. קיבלתי את המבוקש. יאיי! לא חשבתי שאצליח.
<h1>סעיף ב'</h1>
עכשיו נותנים לנו גם מעגל עם מרכז בנקודה {% equation %}M=\left(x_{M},0\right){% endequation %} ומבקשים מאיתנו למצוא את המשוואה שלו - כלומר, צריך למצוא את {% equation %}x_{M}{% endequation %} ואת הרדיוס. הנתון שלנו הוא שהמשיקים לפרבולה משיקים גם למעגל באותן נקודות. אז נראה לי שהגיע הזמן לכתוב במפורש מהן הנקודות. אמרו לנו ש-{% equation %}p=2{% endequation %}, אז נקודות ההשקה הן

{% equation %}K=\left(1,2\right),L=\left(1,-2\right){% endequation %}.

יש לי שתי נקודות על המעגל. האם זה מספיק לי כדי למצוא את המשוואה שלו או שאצטרך להשתמש גם בכך שהמשיקים לפרבולה <strong>משיקים</strong> למעגל ולא סתם חותכים אותו? בואו ננסה קודם לעבוד עם מה שיש. כרגע משוואת המעגל היא {% equation %}\left(x-x_{M}\right)^{2}+y^{2}=R^{2}{% endequation %}. מכיוון ש-{% equation %}y{% endequation %} מופיע רק בריבוע, הצבה של {% equation %}K{% endequation %} והצבה של {% equation %}L{% endequation %} למשוואה הזו יתנו לי את אותו דבר בדיוק: {% equation %}\left(1-x_{M}\right)^{2}+4=R^{2}{% endequation %}. זה לא מספיק טוב, צריך עוד משוואה.

אם כן, מהו השיפוע של משיק למעגל? נגזור שוב באופן סתום ונקבל {% equation %}2\left(x-x_{M}\right)+2yy^{\prime}=0{% endequation %}, כלומר {% equation %}y^{\prime}=-\frac{x-x_{M}}{y}{% endequation %}. כבר ראינו שהשיפוע של הישרים שלנו הוא {% equation %}1,-1{% endequation %} ולכן בואו ננסה להציב אחד מהם:

{% equation %}1=-\frac{1-x_{M}}{2}{% endequation %}

וקיבלנו ש-{% equation %}x_{M}=3{% endequation %}. נציב את זה במשוואה {% equation %}\left(1-x_{M}\right)^{2}+4=R^{2}{% endequation %} ונקבל {% equation %}R^{2}=8{% endequation %}. כלומר, משוואת המעגל היא {% equation %}\left(x-3\right)^{2}+y^{2}=8{% endequation %}.
<h1>סעיף ג'</h1>
עכשיו מגיע עוד משהו שאין לי מושג איך עושים - משוואת מעגל שחסום במרובע. כרגיל, אני מעדיף לנסות להמציא מחדש את הגלגל במקום להסתכל בדף נוסחאות או משהו דומה. אני אומר - משוואת מעגל כללית היא {% equation %}\left(x-x_{0}\right)^{2}+\left(y-y_{0}\right)^{2}=R^{2}{% endequation %}. גוזרים ומקבלים ש-{% equation %}2\left(x-x_{0}\right)+2\left(y-y_{0}\right)y^{\prime}=0{% endequation %}, כלומר ש-{% equation %}y^{\prime}=-\frac{x-x_{0}}{y-y_{0}}{% endequation %} היא המשוואה לשיפוע המשיק שעובר דרך {% equation %}\left(x,y\right){% endequation %}. אם המעגל חסום במרובע זה נותן לי <strong>ארבעה</strong> משיקים שאני מכיר. בואו ננסה לעשות סדר ולכתוב הכל במפורש:

{% equation %}A=\left(-1,0\right){% endequation %}

{% equation %}M=\left(3,0\right){% endequation %}

{% equation %}K=\left(1,2\right){% endequation %}

{% equation %}L=\left(1,-2\right){% endequation %}

{% equation %}\text{AK: }y=x+1{% endequation %}

{% equation %}\text{KM: }y=-x+3{% endequation %}

{% equation %}\text{ML: }y=x-3{% endequation %}

{% equation %}\text{LA: }y=-x-1{% endequation %}

מהמשוואות ברור שזה לא סתם מרובע אלא מלבן, כי הצלעות ניצבות זו לזו. מדידת אורכי הצלעות מראה שזה ריבוע עם אורך צלע 2. האם זה עוזר לי איכשהו? סביר להניח שכן - הסימטריה גוררת שמרכז המעגל יהיה גם מרכז הריבוע. האם מותר לי להשתמש בשיקולי סימטריה שכאלו פה? בואו נניח שכן כי אין לי מושג איך לפתור אחרת. בעזרת סימטריה כל מה שאני צריך לעשות הוא למצוא את מרכז הריבוע. הדרך שנראית לי הכי בטוחה לעשות את זה היא למצוא את האלכסונים {% equation %}\text{AM}{% endequation %} ו-{% equation %}\text{KL}{% endequation %} ולבדוק מהי נקודת החיתוך שלהם. המשוואות שלהם הן {% equation %}y=0{% endequation %} ו-{% equation %}x=1{% endequation %}, כך שנקודת החיתוך היא פשוט ב-{% equation %}\left(1,0\right){% endequation %}. והרדיוס? מספיק לי לחשב את המרחק מ-{% equation %}\left(1,0\right){% endequation %} לאמצע של אחת מצלעות הריבוע, נאמר אל {% equation %}\left(0,1\right){% endequation %} שהוא אמצע הצלע {% equation %}\text{AK}{% endequation %}. המרחק בבירור מקיים {% equation %}R^{2}=2{% endequation %}, כך שמשוואת המעגל היא {% equation %}\left(x-1\right)^{2}+y^{2}=2{% endequation %}.
<h1>מה דעתי על השאלה?</h1>
לטעמי זו שאלה טובה, אם מקבלים את זה שכדאי ללמוד גאומטריה אנליטית, ולדעתי כדאי ללמוד גאומטריה אנליטית. אבל קצת הפריע לי שאין לי מושג איך פותרים את ג' בדרך כללית, אם זה אפשרי בכלל. לא כי זה פוגם בשאלה עבורי, אלא כי אני לא בטוח מה תלמיד בית ספר עושה כשהוא צריך להתמודד עם שאלה כמו זו.
<h1>שאלה 2</h1>
<a href="{{site.baseurl}}{{site.post_images}}/2017/01/2-question2.png" rel="attachment wp-att-3406"><img class="aligncenter size-full wp-image-3406" src="{{site.baseurl}}{{site.post_images}}/2017/01/2-question2.png" alt="2-question2" width="864" height="293" /></a>

הא, שאלת וקטורים. הנה וידוי אפל: זו לא הפעם הראשונה שבה השתעשעתי במחשבה על כתיבת פוסט פתרון בגרות. בפעם הקודמת ניגשתי לבגרות אקראית, ניסיתי קודם כל לפתור את שאלת הוקטורים שלהם, כי "פחחח זה כמו אלגברה לינארית אני אוכל את זה בלי מלח", ואז לא הצלחתי לפתור אותה. בכלל. בואו נראה אם זה מה שיקרה גם הפעם...
<h1>סעיף א'</h1>
להודות על האמת? גם הפעם אין לי מושג איך <strong>אמורים</strong> לפתור את השאלה הזו. וקטורים זה לא נושא שלמדתי אי פעם בתיכון. אבל איך אני פותר את השאלה? ובכן, בנקודה שבה הישר משיק למעגל הרדיוס של המעגל מאונך אליו. בהינתן ישר ונקודה, האנך לישר הזה שעובר דרך הנקודה הוא <strong>המרחק</strong> של הנקודה מהישר - האורך של האנך הוא המינימלי מבין אורכי כל הקווים מהנקודה אל הישר. אז יש לנו פה בעיית מינימיזציה פשוטה. נגדיר פונקציה

{% equation %}f\left(t\right)=\left|B-O\right|^{2}=\left|\left(2+t,2+2t,t\right)-\left(0,0,0\right)\right|=\left(2+t\right)^{2}+\left(2+2t\right)^{2}+t^{2}=6t^{2}+6t+8{% endequation %}

נגזור ונקבל {% equation %}f^{\prime}\left(t\right)=6t+6{% endequation %}. נשווה לאפס ונקבל {% equation %}t=-1{% endequation %}. לכן {% equation %}B=\left(2-1,2-2,-1\right)=\left(1,0,-1\right){% endequation %}.

זה היה מאוד קל, אבל השתמשתי פה בחדו"א; אני מנחש שבתיכון לומדים את הנוסחה למרחק נקודה מישר או משהו ומשתמשים בזה.
<h1>סעיף ב'</h1>
נתחיל בלנסות להבין איך בדיוק נראה המעגל. מה הרדיוס שלו? אנחנו יודעים ש-{% equation %}B=\left(1,0,-1\right){% endequation %} נמצאת על המעגל, כך שרדיוס המעגל הוא {% equation %}\sqrt{1^{2}+0^{2}+\left(-1\right)^{2}}=\sqrt{2}{% endequation %}. אם נמצא את {% equation %}A{% endequation %} ונראה שזה המרחק שלה מראשית הצירים, סיימנו. אבל איך עושים את זה? צריך למצוא את המישור {% equation %}\pi{% endequation %} איכשהו. נתונים לנו שני ישרים במישור: {% equation %}l_{1}{% endequation %} וגם הרדיוס של המעגל. המישור גם עובר דרך ראשית הצירים אז אין צורך להזיז אותו במיוחד (על ידי חיבור של נקודה שונה מאפס אל הצירוף הלינארי של שני הישרים הללו). כעת, את הישר {% equation %}l_{1}{% endequation %} נזיז אל ראשית הצירים ונקבל את הוקטור {% equation %}\left(1,2,1\right){% endequation %}. הרדיוס מתואר על ידי הוקטור {% equation %}\left(1,0,-1\right){% endequation %} (שהוא בעצם הנקודה {% equation %}B{% endequation %}). לכן משוואת המישור היא {% equation %}\pi:t_{1}\left(1,2,1\right)+t_{2}\left(1,0,-1\right){% endequation %}. אנחנו רוצים למצוא חיתוך בין זה ובין {% equation %}\left(0,1,1\right)+s\left(2,-1,1\right){% endequation %}. כלומר, יש לנו מערכת משוואות בשלושה נעלמים {% equation %}\left(t_{1},t_{2},s\right){% endequation %} ועם שלוש משוואות (עבור קואורדינטות {% equation %}x,y,z{% endequation %}). אפשר לכתוב זאת כך: {% equation %}t_{1}\left(1,2,1\right)+t_{2}\left(1,0,-1\right)=s\left(2,-1,1\right)+\left(0,1,1\right){% endequation %} ואחרי העברת אגפים נקבל {% equation %}t_{1}\left(1,2,1\right)+t_{2}\left(1,0,-1\right)+s\left(-2,1,-1\right)=\left(0,1,1\right){% endequation %}.

ברשותכם אכתוב את זה כמטריצה:

{% equation %}\left(\begin{array}{ccc}1 & 1 & -2\\2 & 0 & 1\\1 & -1 & -1\end{array}\right)\left(\begin{array}{c}t_{1}\\t_{2}\\s\end{array}\right)=\left(\begin{array}{c}0\\1\\1\end{array}\right){% endequation %}

נחסיר את השורה הראשונה משתי האחרות (מהשניה, כשהראשונה מוכפלת פי 2) ונקבל

{% equation %}\left(\begin{array}{ccc}1 & 1 & -2\\0 & -2 & 5\\0 & -2 & 1\end{array}\right)\left(\begin{array}{c}t_{1}\\t_{2}\\s\end{array}\right)=\left(\begin{array}{c}0\\1\\1\end{array}\right){% endequation %}

עכשיו נשתמש בשורה השלישית כדי לאפס את הקואורדינטה השניה בשתי האחרות:

{% equation %}\left(\begin{array}{ccc}1 & 0 & -\frac{3}{2}\\0 & 0 & 4\\0 & 1 & -\frac{1}{2}\end{array}\right)\left(\begin{array}{c}t_{1}\\t_{2}\\s\end{array}\right)=\left(\begin{array}{c}\frac{1}{2}\\0\\-\frac{1}{2}\end{array}\right){% endequation %}

בגלל שקיבלנו 0 בעמודת התוצאה בשורה השניה אנחנו יכולים להשתולל איתה חופשי ולאפס את שאר השורות בקואורדינטה הזו בלי לשנות את התוצאה. נקבל:

{% equation %}\left(\begin{array}{ccc}1 & 0 & 0\\0 & 0 & 1\\0 & 1 & 0\end{array}\right)\left(\begin{array}{c}t_{1}\\t_{2}\\s\end{array}\right)=\left(\begin{array}{c}\frac{1}{2}\\0\\-\frac{1}{2}\end{array}\right){% endequation %}

הפתרון פה הוא חד משמעי: {% equation %}t_{1}=\frac{1}{2},t_{2}=-\frac{1}{2}{% endequation %} ו-{% equation %}s=0{% endequation %}. מה שנחמד הוא שקל לבדוק את הפתרון הזה במפורש על ידי הצבה:

{% equation %}\frac{1}{2}\left(1,2,1\right)-\frac{1}{2}\left(1,0,-1\right)+0\left(-2,1,-1\right)=\left(\frac{1}{2}-\frac{1}{2},1-0,\frac{1}{2}+\frac{1}{2}\right)=\left(0,1,1\right){% endequation %}, כמבוקש.

קיבלנו, אם כן, שנקודת החיתוך היא {% equation %}A=\left(0,1,1\right){% endequation %} עצמה. מכיוון ש-{% equation %}\left|\left(0,1,1\right)-\left(0,0,0\right)\right|=\sqrt{2}{% endequation %} קיבלנו שהיא אכן על המעגל. נותר רק למצוא את השטח של המשולש {% equation %}\text{AOB}{% endequation %}. וזו שאלה מעניינת בפני עצמה בשבילי - איך מוצאים שטח של משולש בתלת מימד כשנתונות לי רק הקואורדינטות של הקודקודים שלו? אני זוכר במעורפל שזה קשור למכפלה וקטורית (ליתר דיוק, אני זוכר שזו מכפלת אורכי הוקטורים בסינוס הזווית ביניהם ואני זוכר שהדבר הזה הוא מכפלה וקטורית), ובדיקה זריזה מעלה שאכן כך הדבר - מכפילים וקטורית שתי צלעות של המשולש, לוקחים את גודל הוקטור שהתקבל, מחלקים ב-2. אויש, אני שונא מכפלות וקטורית. טוב, בואו נעשה את זה, אני זוכר את "שיטת הדטרמיננטה" לחישוב:

{% equation %}\left|\begin{array}{ccc}\hat{x} & \hat{y} & \hat{z}\\1 & 0 & -1\\0 & 1 & 1\end{array}\right|=1\cdot\hat{x}-1\cdot\hat{y}+1\cdot\hat{z}{% endequation %}

ולכן קיבלנו שטח של {% equation %}\frac{\sqrt{1^{2}+1^{2}+1^{2}}}{2}=\frac{\sqrt{3}}{2}{% endequation %}.
<h1>מה דעתי על השאלה?</h1>
בכל הנושא הזה של וקטורים יש לי תחושה ש"עוברים ליד" אלגברה לינארית אבל לא באמת נוגעים בה - לא באמת יצא לי לפתור תרגילים כמו זה אי פעם. מצד שני, אלגברה לינארית מופשטת יותר זה משהו שכנראה אי אפשר ללמד בבית הספר, ואילו החומר הזה נראה לי אפילו שימושי למי שהולכים לתחומים יותר פיזיקליים/הנדסיים באופיים. קשה לי להתלונן.
<h1>שאלה 3</h1>
<img class="aligncenter size-full wp-image-3407" src="{{site.baseurl}}{{site.post_images}}/2017/01/2-question3.png" alt="2-question3" width="928" height="559" />
<h1>סעיף א'</h1>
נתון לנו מספר מרוכב מחריד, אבל מן הסתם אפשר לפשט אותו. אני לא זוכר מתי לאחרונה כתבתי {% equation %}\text{CIS}{% endequation %} ואין לי כוונה להתחיל עכשיו - אשתמש בסימון הסטנדרטי יותר במתמטיקה, {% equation %}e^{i\theta}=\cos\theta+i\sin\theta{% endequation %}. בסימון הזה המונה הוא {% equation %}e^{i\left(\pi/9\right)}{% endequation %} ואילו המכנה הוא... אה, יש מינוס ליד הסינוס. זה אומר שלוקחים מינוס של כל הזווית, כלומר המכנה הוא {% equation %}e^{-i\left(\pi/12\right)}{% endequation %}. עכשיו קל לבצע העלאה בחזקה - פשוט כופלים את המעריך של האקספוננט בחזקה הזו, כמו בחוקי חזקות רגילים, וגם חלוקה מתבצעת בדרך דומה:

{% equation %}z=\frac{\left(e^{i\frac{\pi}{9}}\right)^{3}}{\left(e^{-i\frac{\pi}{12}}\right)^{2}}=\frac{e^{i\frac{\pi}{3}}}{e^{-i\frac{\pi}{6}}}=e^{i\left(\frac{\pi}{3}+\frac{\pi}{6}\right)}=e^{i\frac{\pi}{2}}{% endequation %}

כעת, {% equation %}\left|z\right|=1{% endequation %} (כי ה-{% equation %}e{% endequation %} בחזקת {% equation %}i{% endequation %}-משהו לא מוכפל בשום מספר ממשי שונה מ-1) ואילו הארגומנט של {% equation %}z{% endequation %} הוא {% equation %}\frac{\pi}{2}{% endequation %}.

קל לחשב את החזקה {% equation %}z^{n}{% endequation %} כעת: {% equation %}z^{n}=e^{i\frac{n\pi}{2}}{% endequation %}. כדי לקבל מספר מדומה טהור, הארגומנט מודולו {% equation %}2\pi{% endequation %} צריך להיות {% equation %}\frac{\pi}{2}{% endequation %} או {% equation %}\frac{3\pi}{2}{% endequation %} (אני זוכר את זה גאומטרית - צריך שהסיבוב של המספר המרוכב ביחס לציר {% equation %}x{% endequation %} יהיה של 90 מעלות או 270 מעלות, כך שנחים על ציר {% equation %}y{% endequation %}). כלומר, {% equation %}n\equiv1,3\left(\text{mod }4\right){% endequation %}, או בסימון שאולי יותר אוהבים בתיכון - {% equation %}n=1+4k{% endequation %} או {% equation %}n=3+4k{% endequation %} (למעשה, זו דרך מסורבלת לומר ש-{% equation %}n{% endequation %} אי זוגי, אבל זה מה שקפץ לי לראש ולא ניסיתי לפשט).
<h1>סעיף ב'</h1>
ממבט חטוף על המקום הגאומטרי אין לי מושג קלוש מה הוא. אז בואו ננסה לפשט. אני זוכר את הנוסחאות החביבות הבאות: {% equation %}z+\overline{z}=2\text{Re}z{% endequation %} ו-{% equation %}z-\overline{z}=2\text{Im}z{% endequation %}. אם כן, אפשר לכתוב את המקום הגאומטרי גם בתור {% equation %}\left|\text{Re}z-m\text{Im}z\right|=20{% endequation %}.

רגע, לא, פסק זמן.

לכתוב {% equation %}\left|\text{Re}z-m\text{Im}z\right|=20{% endequation %} זה <strong>שגוי לגמרי</strong> ואני עשיתי את הטעות הזו בכל זאת ופתרתי את התרגיל על פי זה וקיבלתי פתרון <strong>שגוי</strong>. אחסוך מכם את הפתרון הזה. יש לנו כאן דוגמה קלאסית לפאשלת חוסר תשומת לב של "כן, ברור שאני יודע את זה". איפה טעיתי? הנוסחה {% equation %}z-\overline{z}=2\text{Im}z{% endequation %} לא נכונה; מה שנכון הוא {% equation %}z-\overline{z}=2i\cdot\text{Im}z{% endequation %}. כלומר, זה מוכפל ב-{% equation %}i{% endequation %}, מה שמשנה לגמרי את ההמשך. אוי ווי. בכל מה שקרה אחרי הטעות הזו לא פקפקתי בכלל במה שכתבתי ולא היה לי איך לבדוק את עצמי. פשוט פאשלה מביכה.

אוקיי, עכשיו משעליתי על הטעות בדיעבד, מה הפתרון הנכון? ובכן, חזרה אל הנוסחה שהגענו אליה: {% equation %}\left|\text{Re}z-mi\cdot\text{Im}z\right|=20{% endequation %}. בואו נחשוב על {% equation %}z{% endequation %} בתור נקודה ב-{% equation %}\mathbb{R}^{2}{% endequation %}, כלומר במקום לכתוב {% equation %}z=x+iy{% endequation %} נכתוב {% equation %}\left(x,y\right){% endequation %}. אז הנוסחה היא {% equation %}\left|x-miy\right|=20{% endequation %}, ועל פי נוסחת הערך המוחלט של מרוכבים זה אומר {% equation %}x^{2}+\left(my\right)^{2}=400{% endequation %}. זה נראה כמו משוואת מעגל מוזרה - בפועל אני יודע שזו משוואת אליפסה, אבל גם שדרך ההצגה הזו היא לא דרך ההצגה ה"סטנדרטית" של משוואת אליפסה. הייתי צריך להזכיר לעצמי (על ידי גיגול) שהמשוואה של אליפסה שהצירים שלה נמצאים על צירי {% equation %}x,y{% endequation %} היא {% equation %}\frac{x^{2}}{a^{2}}+\frac{y^{2}}{b^{2}}=1{% endequation %} כאשר {% equation %}a,b{% endequation %} הם פרמטרים של האליפסה: נקודות החיתוך של האליפסה עם הצירים הן בדיוק {% equation %}\pm\left(a,0\right){% endequation %} ו-{% equation %}\pm\left(0,b\right){% endequation %}. במקרה הנוכחי, אם כן, נחלק ב-{% equation %}20^{2}{% endequation %} את שני האגפים ונקבל {% equation %}\frac{x^{2}}{20^{2}}+\frac{y^{2}}{\left(20m^{-1}\right)^{2}}=1{% endequation %}, דהיינו אצלנו {% equation %}a=20{% endequation %} ו-{% equation %}b=\frac{20}{m}{% endequation %}.

מה שמבקשים מאיתנו כעת הוא למצוא את {% equation %}a,b{% endequation %} בהינתן שהנקודה {% equation %}\left(12,8\right){% endequation %} נמצאת על האליפסה. בפועל אני צריך למצוא את {% equation %}m{% endequation %} כך שיותר קל לי לחזור למשוואה {% equation %}x^{2}+\left(my\right)^{2}=400{% endequation %}. נציב את {% equation %}x,y{% endequation %} ונקבל {% equation %}144+64m^{2}=400{% endequation %}, כלומר {% equation %}9+4m^{2}=25{% endequation %} (עשיתי את החישובים בראש! הא!), כלומר {% equation %}m^{2}=4{% endequation %}, כלומר {% equation %}m=2{% endequation %} (לא ייתכן ש-{% equation %}m=-2{% endequation %} כי אמרו לנו במפורש שהוא חיובי). מכאן ש-{% equation %}a=20,b=10{% endequation %} ולכן נקודות החיתוך הן {% equation %}\left(20,0\right),\left(-20,0\right),\left(0,10\right),\left(0,-10\right){% endequation %}.
<h1>מה דעתי על השאלה?</h1>
האמת, לא משהו. וזה לא קשור לכך שבסעיף ב' טעיתי באופן מזעזע ומביך! נשבע!

הבעיה בשאלה הזו היא שהיא כמעט לא עוסקת במספרים מרוכבים. טוב, בסעיף א' צריך להבין את ההצגה הקוטבית של מספרים מרוכבים וכפועל יוצא מכך את כללי ההעלאה בחזקה והחילוק, אבל בסעיף ב' כל מה שצריך לדעת הוא את ההגדרה של ערך מוחלט ואת הנוסחאות הללו לסכום והפרש עם הצמוד (כפי שראינו, גם אני לא באמת זכרתי אותן...). מעבר לכך רוב סעיף ב' הוא בכלל שאלה נוספת בגאומטריה אנליטית (באופן חוקי מותר להם לעשות את זה ; הפרק כולו עוסק בגאומטריה אנליטית ומרוכבים, אין התחייבות לשאלה אחת על זה ושאלה אחרת על ההוא).

מצד שני, אולי זה בעצם בסדר? על מה בדיוק אפשר לשאול כשמדובר על מספרים מרוכבים מעבר לרמת ההגדרות הבסיסיות? משפט אינטגרל קושי? ואני כן חושב שכדאי לראות מספרים מרוכבים בבית הספר כדי להיות מודעים לקיום היצורים הללו. אז יש סיכוי טוב שאני מתלונן על כלום.
<h1>שאלה 4</h1>
<a href="{{site.baseurl}}{{site.post_images}}/2017/01/2-question4.png" rel="attachment wp-att-3408"><img class="aligncenter size-full wp-image-3408" src="{{site.baseurl}}{{site.post_images}}/2017/01/2-question4.png" alt="2-question4" width="937" height="533" /></a>

הא. שוב חדו"א. אף פעם לא הבנתי למה יש שני סוגי חדו"א בבגרות. כאילו, מה כבר ההבדל הגדול בין שניהם?
<h1>סעיף א'</h1>
כבר התחלה טובה - אין לי מושג איך מוצאים את נקודות החיתוך עם הצירים של {% equation %}f\left(x\right)=9^{x}-2\cdot3^{x}-3{% endequation %}. טוב, שניה, בואו לא נתייאש כל כך מהר. מה שמייד קופץ לי לעיניים הוא ש-{% equation %}9=3^{2}{% endequation %} כך שאפשר לכתוב {% equation %}f\left(x\right)=\left(3^{x}\right)^{2}-2\cdot3^{x}-3{% endequation %}. קיבלנו פה משוואה ריבועית במשתנה {% equation %}t=3^{x}{% endequation %}, כלומר {% equation %}t^{2}-2t-3=0{% endequation %}. את זה קל לי לפתור ולקבל {% equation %}t_{1,2}=\frac{2\pm\sqrt{4+12}}{2}=\frac{2\pm4}{2}=1\pm2=3,-1{% endequation %}. עבור{% equation %}3^{x}=3{% endequation %} הפתרון הוא כמובן {% equation %}x=1{% endequation %}; ואילו למשואוה {% equation %}3^{x}=-1{% endequation %} אין פתרון. לכן יש נקודת חיתוך יחידה עם הצירים: {% equation %}x=1{% endequation %}.

עכשיו לאסימפטוטה אופקית. מה זו אסימפטוטה אופקית? אני מניח שהכוונה לקו האופקי ({% equation %}y=c{% endequation %} עבור {% equation %}c{% endequation %} כלשהו) שהפונקציה שואפת אליו כש-{% equation %}x{% endequation %} שואף לאינסוף או מינוס אינסוף. כש-{% equation %}x{% endequation %} שואף לאינסוף בבירור הפונקציה שואפת לאינסוף, אבל כשהוא שואף למינוס אינסוף אז {% equation %}9^{x}\to0{% endequation %} וגם {% equation %}3^{x}\to0{% endequation %} ולכן נקבל שאיפה ל-{% equation %}-3{% endequation %}. כלומר, {% equation %}y=-3{% endequation %} הוא האסימפטוטה.

בשביל נקודות קיצון צריך לגזור. העניין הוא שאני לא זוכר איך גוזרים פונקציה מעריכית. אני זוכר ש-{% equation %}\left(e^{x}\right)^{\prime}=e^{x}{% endequation %}, אבל לא מה קורה כשהבסיס הוא {% equation %}a{% endequation %}. טוב, אני משקר, אני כן זוכר במעורפל שכופלים ב-{% equation %}\ln a{% endequation %} אבל אני לא בטוח בזה. אפשר לבדוק בדף נוסחאות ואפשר לפתח את זה מחדש. אני יודע ש-{% equation %}e^{\ln a}=a{% endequation %} כי זו ההגדרה של {% equation %}\ln{% endequation %} פחות או יותר (האמת שמבחינתי ההגדרה של {% equation %}\ln x{% endequation %} היא משהו מפלצתי עם אינטגרלים אבל נעזוב את זה). לכן {% equation %}a^{x}=\left(e^{\ln a}\right)^{x}=e^{x\ln a}{% endequation %} ומכאן ברור ש-{% equation %}\left(a^{x}\right)^{\prime}=\left(e^{x\ln a}\right)^{\prime}=\ln a\cdot\left(e^{x\ln a}\right)=a^{x}\ln a{% endequation %}. יופי, אז בואו נגזור:

{% equation %}f^{\prime}\left(x\right)=2\cdot3^{x}\cdot3^{x}\cdot\ln3-2\cdot3^{x}\cdot\ln3=2\ln3\left(\left(3^{x}\right)^{2}-3^{x}\right){% endequation %}

שוב אסמן {% equation %}t=3^{x}{% endequation %} ואקבל שהנגזרת מתאפסת אם {% equation %}t^{2}=t{% endequation %}, כלומר כש-{% equation %}t=0{% endequation %} (לא הולך לקרות עבור {% equation %}t=3^{x}{% endequation %}) או אם {% equation %}t=1{% endequation %}, מה שקורה כש-{% equation %}x=0{% endequation %}. אז {% equation %}0{% endequation %} היא נקודת קיצון, אבל האם מינימום או מקסימום? לפני שאני מחשב נגזרת שניה וכאלה בואו נחשוב רגע - כאשר {% equation %}x{% endequation %} הולך וגדל גם הפונקציה הולכת וגדלה. לכן אם כבר יש פה נקודת קיצון היא תהיה נקודת מינימום. כש-{% equation %}x=0{% endequation %} הערך של הפונקציה הוא {% equation %}1-2-3=-4{% endequation %} וכשאיקס שואף למינסוף אינסוף הפונקציה שואפת ל-{% equation %}-3{% endequation %}, כך שגם זה עוזר לי לראות שיש פה מינימום. והנגזרת השניה? היא {% equation %}2\ln3\left(2\ln3\cdot\left(3^{x}\right)^{2}-\ln3\cdot3^{x}\right)=2\ln^{2}3\left(2\left(3^{x}\right)^{2}-3^{x}\right){% endequation %} ולכן כשנציב {% equation %}x=0{% endequation %} נקבל משהו חיובי - מתאים לכך שזו נקודת מינימום. שימו לב שהנגזרת השניה מתאפסת כאשר {% equation %}2t^{2}=t{% endequation %}, כלומר ב-{% equation %}t=0{% endequation %} (שלא יכול לקרות, כזכור) או ב-{% equation %}t=\frac{1}{2}{% endequation %}, כלומר {% equation %}3^{x}=\frac{1}{2}{% endequation %}, כלומר ב-{% equation %}x=\log_{3}\frac{1}{2}{% endequation %}. זה לא כל כך מעניין מה המספר המדויק הזה פרט לכך שהוא שלילי. בנקודה הזו יקרה לגרף הפונקציה דבר מוזר - היא תעבור מקמירות לקעירות. זה משהו הכרחי- כי השאיפה של הפונקציה לאסימפטוטה כשאיקס שואף למינוס אינסוף מכריח אותה להיות קעורה, בזמן שהשאיפה של הפונקציה לאינסוף כשאיקס שואף לאינסוף מכריחה אותה להיות קמורה. כך שמעבר מקעירות לקמירות חייב להתקיים. הנקודה שמעניינת אותי הוא שהמעבר הזה לא מתקיים ב-{% equation %}x=0{% endequation %} אלא לפניו.

נשאר לצייר סקיצה. בסקיצה אני מתחשב בדברים הבאים: א) נקודת המינימום ב) האסימפטוטה ג) נקודת החיתוך עם ציר {% equation %}y{% endequation %} ב-{% equation %}x=1{% endequation %} ד) כל הדיון שניהלתי למעלה על קמירות וקעירות. הנה הסקיצה:

<a href="{{site.baseurl}}{{site.post_images}}/2017/01/sketch4.png" rel="attachment wp-att-3411"><img class="aligncenter size-full wp-image-3411" src="{{site.baseurl}}{{site.post_images}}/2017/01/sketch4.png" alt="sketch4" width="343" height="311" /></a>
<h1>סעיף ב'</h1>
הייתה לי טעות מטופשת במיוחד בסעיף הזה - חישבתי בהתחלה את השטח הלא נכון. במקום לחשב את השטח שמוגבל על ידי גרף הפונקציה <strong>מתחת</strong> לאסימפטוטה, חישבתי את זה ש<strong>מעל</strong> האסימפטוטה. זו אשמתי המלאה - קריאה לא נכונה של התיאור שלהם את השטח שאמורים לחשב. זו כבר טעות מפגרת שניה שלי במבחן. האם זה אומר שאני פותר אותו בשעות מאוחרות מדי? האם בזמן אמת הייתי עושה את אותן טעויות? לא יודע.

בואו נפתור את השאלה הנכונה. מה שאנחנו רוצים הוא לחשב את <strong>מינוס</strong> האינטגרל מ-{% equation %}x=0{% endequation %} ועד ל-{% equation %}x{% endequation %} שהוא נקודת החיתוך של הפונקציה עם האסימפטוטה (הקו האדום אצלי). אם כן, צריך להתחיל מלשאול את עצמנו מהי נקודת החיתוך הזו. כלומר מתי {% equation %}f\left(x\right)=-3{% endequation %}, כלומר מתי {% equation %}\left(3^{x}\right)^{2}-2\cdot3^{x}-3=-3{% endequation %}, כלומר מתי {% equation %}t^{2}=2t{% endequation %}. כרגיל, {% equation %}t=0{% endequation %} נפסל ולכן נקבל {% equation %}t=2{% endequation %}, כלומר {% equation %}3^{x}=2{% endequation %}, כלומר {% equation %}x=\log_{3}2{% endequation %}. בנקודה הזו {% equation %}9^{x}=4{% endequation %} ואילו {% equation %}3^{x}=2{% endequation %} וזה אכן מסתדר.

עכשיו, שימו לב שהאינטגרל הזה ייתן לי <strong>יותר מדי</strong> שטח, כי האינטגרל מודד את השטח שכלוא בין גרף הפונקציה לבין ציר {% equation %}x{% endequation %}. כאן אני צריך למדוד את השטח שכלוא בין גרף הפונקציה ובין האסימפטוטה. יש שתי דרכים לעשות זאת: אפשר לחשב את האינטגרל הרגיל ואז להחסיר את שטח המלבן שספרתי "בטעות", ואפשר פשוט "להרים" את הפונקציה על ידי כך שאחשב את האינטגרל של {% equation %}f\left(x\right)+3=9^{x}-2\cdot3^{x}{% endequation %}, חישוב שיהיה לי יותר פשוט. תדמיינו שאני לוקח את גרף הפונקציה כולה ודוחף אותו למעלה, יחד עם קו האסימפטוטה והכל, כדי להבין למה זה יעבוד.

אם כן, האינטגרל שלי הוא:

{% equation %}\int_{0}^{\log_{3}2}\left(9^{x}-2\cdot3^{x}\right)dx=\left[\frac{9^{x}}{\ln9}-\frac{2\cdot3^{x}}{\ln3}\right]_{0}^{\log_{3}2}={% endequation %}

{% equation %}=\left(\frac{4}{2\ln3}-\frac{2\cdot2}{\ln3}\right)-\left(\frac{1}{2\ln3}-\frac{2}{\ln3}\right){% endequation %}

{% equation %}=\left(-\frac{4}{2\ln3}\right)-\left(-\frac{3}{2\ln3}\right){% endequation %}

{% equation %}=-\frac{1}{2\ln3}{% endequation %}

ולכן הפתרון, שהוא כאמור מינוס האינטגרל הזה, הוא {% equation %}\frac{1}{2\ln3}{% endequation %}
<h1>סעיף ג'</h1>
כאן עושים התחכמות ומרימים את {% equation %}f{% endequation %} עוד קצת. מה שצריך להבין פה הוא שכשמרימים את הפונקציה {% equation %}f{% endequation %} זה לא משנה את השטח שכלוא בינה, בין ציר {% equation %}y{% endequation %} ובין הקו הישר של האסימפטוטה, אחרי שאנחנו מרימים גם את הקו הישר הזה. מה שעשיתי בסעיף הקודם היה להרים את הקו של האסימפטוטה כך שינוח על ציר {% equation %}x{% endequation %}; בסעיף הזה הם מרימים אותו עוד קצת, כך שהוא הופך להיות הישר {% equation %}y=1{% endequation %}. השטח לא משתנה כתוצאה מכך, ולכן הערך של {% equation %}k{% endequation %} הוא {% equation %}1{% endequation %}.
<h1>מה דעתי על השאלה?</h1>
זו שאלת חדו"א סטנדרטית. כאמור, לא ברור לי מה ההבדל המהותי בינה לבין שאלות החדו"א בחלק א' של המבחן, ואני לא מבין למה צריך כל כך הרבה חדו"א. אז בחלק א' הפונקציות היו טריגונומטריות וכאן הן אקספוננטים. למי אכפת?
<h1>שאלה 5</h1>
<a href="{{site.baseurl}}{{site.post_images}}/2017/01/2-question5.png" rel="attachment wp-att-3409"><img class="aligncenter size-full wp-image-3409" src="{{site.baseurl}}{{site.post_images}}/2017/01/2-question5.png" alt="2-question5" width="688" height="805" /></a>

השאלה הזו מזכירה לי במבט ראשון את השאלה ההיא מחלק א' שאהבתי. בואו נקווה שזה לא יתגלה בתור דמיון שטחי נטו.
<h1>סעיף א'</h1>
טוב, יש המון מה לקרוא ועד שאני מסיים אני כבר לא זוכר כלום, אבל אני מאוד מתרשם לטובה מכך שבמקום לומר "קעורה" ו"קמורה" הם אומרים "קעורה כלפי מטה" ומוסיפים {% equation %}\cap{% endequation %} ו"קעורה כלפי מעלה" ומוסיפים {% equation %}\cup{% endequation %}. ככה באמת קשה להתבלבל (הטרמינולוגיה שאני מכיר היא לומר "קעורה" בשביל "קעורה כלפי מטה" ו"קמורה" בשביל "קעורה כלפי מעלה"; אני זוכר את זה כי אני זוכר ש"קעורה" אמור להיות כמו קערה, רק הפוך. אני בעיקר זוכר את ה"הפוך" הזה כי הוא מרגיז נורא).

מה שמבקשים ממני הוא למצוא את שיעורי ה-{% equation %}x{% endequation %} של נקודות הקיצון של <strong>הנגזרת</strong> של {% equation %}f{% endequation %} (כי את נקודות הקיצון של {% equation %}f{% endequation %} נתנו לי במפורש). נקודת קיצון של {% equation %}f^{\prime}{% endequation %} היא נקודה שבה הפונקציה מפסיקה להיות עולה ומתחילה להיות יורדת, או ההפך. זה בא לידי ביטוי בגרף של {% equation %}f{% endequation %} במעבר מקמירות לקעירות: אם {% equation %}f^{\prime}{% endequation %} היא פונקציה עולה בתחום מסויים, אז {% equation %}f{% endequation %} היא קמורה באותו התחום, ואילו אם {% equation %}f^{\prime}{% endequation %} היא יורדת אז {% equation %}f{% endequation %} היא קעורה.

נקודות המעבר בין קמירות לקעירות הן בדיוק {% equation %}x=-2{% endequation %}, {% equation %}x=2{% endequation %} ו-{% equation %}x=5{% endequation %}. ב-{% equation %}x=-2{% endequation %} וב-{% equation %}x=5{% endequation %} הפונקציה עוברת מקעירות לקמירות, ולכן אלו נקודות שבהן {% equation %}f^{\prime}{% endequation %} עוברת מירידה לעלייה, כלומר אלו נקודות <strong>מינימום</strong>, ואילו ב-{% equation %}x=2{% endequation %} הפונקציה עוברת מקמירות לקעירות ולכן זו נקודת <strong>מקסימום</strong> של {% equation %}f^{\prime}{% endequation %}.
<h1>סעיף ב'</h1>
מכיוון ש-{% equation %}\ln\left(x\right){% endequation %} מוגדרת רק עבור {% equation %}x&gt;0{% endequation %} מקבלים שתחום ההגדרה של {% equation %}g\left(x\right)=\ln\left(f\left(x\right)\right){% endequation %} הוא {% equation %}x&lt;-2{% endequation %} ו-{% equation %}x&gt;2{% endequation %}. ומתי תהיה אסימפטוטה אנכית? אסימפטוטה אנכית פירושה שהפונקציה שואפת לאינסוף או למינוס אינסוף כאשר {% equation %}x{% endequation %} שואף <strong>לנקודה</strong> (ולא לאינסוף). כאן זה יקרה בדיוק עבור {% equation %}x=-2{% endequation %} ועבור {% equation %}x=2{% endequation %} (בשניהם השאיפה היא למינוס אינסוף כי {% equation %}f\left(x\right){% endequation %} שואפת לאפס בנקודות הללו).

נותר לדבר על נקודות קיצון. מכיוון ש-{% equation %}\ln x{% endequation %} היא פונקציה מונוטונית עולה, הרי ש-{% equation %}\ln\left(f\left(x\right)\right){% endequation %} תחלוק את אותן נקודות קיצון עם {% equation %}f\left(x\right){% endequation %}. בתחום ההגדרה של {% equation %}g\left(x\right){% endequation %} נמצאת רק נקודת הקיצון של {% equation %}x=4{% endequation %}, שבה מתקיים {% equation %}f\left(4\right)=3e{% endequation %} ולכן {% equation %}g\left(4\right)=\ln\left(3e\right)=1+\ln3{% endequation %}. זוהי נקודת מקסימום עבור {% equation %}f\left(x\right){% endequation %} ולכן גם עבור {% equation %}g\left(x\right){% endequation %} זוהי נקודת מקסימום.

לסיום, נותר לצייר את הגרף של {% equation %}g{% endequation %}. אומרים לנו משהו על האסימפטוטה האופקית שלה וזה נראה לי מיותר כי את כל זה אפשר לדעת ממה שאמרו לנו על האסימפטוטה האופקית של {% equation %}f{% endequation %}.

בשרטוט אני מתחשב בדברים הבאים: א) תחום ההגדרה ב) האסימפטוטות האנכיות שמצאתי ג) האסימפטוטה האופקית המדוברת ד) נקודת המקסימום ב-{% equation %}x=4{% endequation %} ה) העובדה שהפונקציה עולה ויורדת כמו {% equation %}f{% endequation %}.

<a href="{{site.baseurl}}{{site.post_images}}/2017/01/sketch5.png" rel="attachment wp-att-3410"><img class="aligncenter size-full wp-image-3410" src="{{site.baseurl}}{{site.post_images}}/2017/01/sketch5.png" alt="sketch5" width="321" height="342" /></a>

<strong>מה דעתי על השאלה?</strong>

שוב, שאלת חדו"א סטנדרטית. דומה לזו של חלק א'. נחמדה. לא משהו מיוחד.

<strong>אז מה למדנו מכל זה?</strong>

תמה ונשלמה הבגרות. ראשית, איך הלך לי? יחסית סביר, בהתחשב בכך שלא התכוננתי למבחן, ובכך שלא פתרתי בתנאי מבחן כך שהריכוז שלי היה נמוך ודילגתי מעל שלבים וכדומה. אלו התירוצים שמצדיקים את העובדה שהמון דברים לא זכרתי, והיו לי גם שגיאות מזעזעות. יש כמה שאלות שפתרתי על סמך הידע הקיים שלי למרות שכנראה בבית הספר לומדים דרכים אחרות להתמודד איתם, אבל בהרבה מקרים לא הרגשתי שהידע שלי מסייע במיוחד. אין גם ספק בכך שכמעט כל השאלות היו "לא כיפיות" - לא הזכירו לי את הדברים שאותי אישית מעניינים במתמטיקה. זו לא בדיוק ביקורת על הבגרות כי אני חושב שבגרות על מה שמעניין אותי הייתה מסתיימת באסון עבור התלמידים.

ייתכן שאתם מצפים לאיזה סיכום מעמיק שבו אשטח את התובנות שלי על שיטת הלימוד בבתי הספר וכיצד יש לשנותה מן היסוד. אבל אני בוודאי לא אעשה שום דבר מוזר שכזה. אני מעדיף להסתכל על הדברים החיוביים פה, ויש כמה: ראשית, המבחן הרגיש לי <strong>הוגן</strong> בהחלט - לא שאלות שמטרתן להכשיל או להקשות בכוונה. הרוב היה סטנדרטי ודורש בעיקר היכרות טובה עם החומר ושליטה בו - שזה מה שאמור לקרות בבגרות. שנית, לא מעט שאלות נראו לי עוסקות בנושאים <strong>חשובים</strong>, כאלו שלא הייתי מוותר עליהם. עיקר התמיהה שלי מופנה לכיוון חדו"א, שאני מרגיש שיש הרבה יותר מדי ממנו במבחן.

דבר אחד שאיני יודע כלל, כי לא בדקתי זאת, הוא מה ההבדלים בין המבחנים הללו ובין המבחנים של תלמידי 3 ו-4 יחידות. על פניו אני לא מרגיש שהיה במבחן הזה משהו "מיוחד" ולכן לא בטוח שאני מבין את כל הקמפיינים של השנה שעברה שמטרתם לעודד 5 יחידות לימוד במתמטיקה בתור סוג של כרטיס כניסה לחיים ליקום ובכלל. אני רוצה לנצל את סיום הפוסט הזה כדי להפנות מסר פשוט לתלמידים, בתור מישהו שיש לו קצת נסיון עם מתמטיקה ואוהב אותה: מתמטיקה תיכונית היא לא סוף הסיפור וגם לא עיקר הסיפור. גם אם אתם עושים עכשיו 3 או 4 יחידות. גם אם אתם לא מבינים את החומר. גם אם המתמטיקה שאתם לומדים משעממת או מעצבנת אתכם, אל תראו בזה סוף הסיפור. אל תתנו לזה לסגור לכם את הדלת בפרצוף. אל תתנו לזה לגרום לכם לוותר על דברים בעתיד באופן אוטומטי. מתמטיקה אוניברסיטאית (גם כזו שנלמדת בפני עצמה וגם כזו שנלמדת על מנת לשמש את הסטודנטים בתחומים אחרים) היא אמנם קשה ותובענית, אבל היא גם מתגמלת יותר, וגם אופי הקשיים בה הוא שונה מהותית. אני לא מציע לכולכם לרוץ ללמוד מתמטיקה או אפילו להתעניין בה, אבל אם אתם מגיעים להחלטה בעניין, אני מקווה שהחוויות שלכם מהתיכון לא יהיו הגורם המכריע.

