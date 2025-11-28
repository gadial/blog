---
id: 2702
title: "נגזרת מרוכבת, פונקציות אנליטיות ונוסחאות קושי-רימן"
date: 2013-08-12 20:12:34
layout: post
categories: 
  - אנליזה מתמטית
tags: 
  - אנליזה מרוכבת
  - נגזרת
  - נוסחאות קושי-רימן
---
המושג היסודי בחשבון דיפרנציאלי הוא מושג ה<strong>נגזרת</strong>. כבר הקדשתי לו <a href="http://www.gadial.net/2010/11/21/derivative/">פוסט</a>, אבל אחזור על הרעיון בקצרה: כאשר יש לנו פונקציה {% equation %}f{% endequation %}, אנחנו מעוניינים למדוד את <strong>קצב השינוי</strong> שלה. המושג האינטואיטיבי שלנו הוא זה של <strong>שינוי ממוצע</strong> - מסתכלים על ההפרש בין ערכי הפונקציה בשתי נקודות שונות, ומחלקים אותו בהפרש שבין הנקודות הללו. אם המרחק בין ת"א וחיפה הוא 100 ק"מ, והמרחק בין השעה שבה יצאנו מת"א - 8:00 - לשעה שבה הגענו לחיפה - 10:00 - הוא 2 שעות, אז השינוי הממוצע של פונקציית המיקום שלנו (פונקציה שמקבלת נקודת זמן ומחזירה את המיקום שלנו באותה נקודת זמן) בין שתי הנקודות הללו של 8:00 ו-10:00 הוא {% equation %}\frac{100}{2}=50{% endequation %}, כשהיחידות שבהן אנו מבצעים את המדידה הן ק"מ לשעה (במתמטיקה הפונקציות הן לרוב אבסטרקטיות - מקבלות מספרים חסרי יחידות ומחזירות מספרים חסרי יחידות - ולכן אנחנו לא מדברים על יחידות רוב הזמן). הבעיה בשינוי ממוצע שכזה היא בכך שהוא מתאר מה קרה לאורך פרק זמן ארוך כלשהו - הוא לא אומר לנו מה קרה בנקודת זמן מסויימת (כלומר, מה היינו רואים אם היינו מסתכלים במד המהירות בנקודת זמן כלשהי).

הדרך הנאיבית להתמודד עם הבעיה היא לומר - אוקיי, אז בואו נשתמש באותו תעלול שהשתמשנו בו עד כה. חישבנו את השינוי הממוצע בין ערך הפונקציה ב-{% equation %}x{% endequation %} ובין ערכה ב-{% equation %}y{% endequation %} על ידי הנוסחה {% equation %}\frac{f\left(x\right)-f\left(y\right)}{x-y}{% endequation %}? יופי, בואו נציב {% equation %}x=y{% endequation %} ונראה מה נקבל. לרוע המזל, נקבל ביטוי מהצורה {% equation %}\frac{0}{0}{% endequation %} וביטוי כזה אינו מוגדר, ואין דרך טובה להגדיר אותו בצורה חד משמעית. אנחנו צריכים לנקוט בגישה קצת יותר חכמה כדי לחקור את {% equation %}f{% endequation %}.

הפתרון הוא כזה: כדי לדעת מה קצב השינוי של הפונקציה {% equation %}f{% endequation %} בנקודה {% equation %}x{% endequation %}, מוסיפים ל-{% equation %}x{% endequation %} ערך <strong>קטן מאוד אך לא אפס</strong> שאפשר לסמן ב-{% equation %}dx{% endequation %}, ואז מחשבים את {% equation %}\frac{f\left(x+dx\right)-f\left(x\right)}{dx}{% endequation %}. זה מה שניוטון ולייבניץ עשו. לרוע המזל, הפתרון הזה לא מוגדר עד הסוף מבחינה מתמטית - לא ברור מה בדיוק אומר מתמטית "קטן מאוד אך לא אפס", ואיך עובדים עם יצור כזה מבחינה טכנית - ניוטון ולייבניץ פשוט התייחסו אליו כאל אפס כשהיה נוח להם, ואל משהו שאינו אפס כשהיה נוח להם. אפשר לבצע פורמליזציה מתמטית של יצור כזה, אבל הגישה הסטנדרטית באנליזה היא שונה ומשתמשת במושג ה<strong>גבול</strong>. הרעיון הבסיסי הוא לקחת ערך מספרי קונקרטי {% equation %}h{% endequation %}, לחשב את {% equation %}\frac{f\left(x+h\right)-f\left(x\right)}{h}{% endequation %}, ואז לשאול את עצמנו לאיזה ערך הביטוי הזה <strong>שואף</strong> כאשר {% equation %}h{% endequation %} שואף לאפס. פורמלית וטכנית, מחשבים את הגבול {% equation %}\lim_{h\to0}\frac{f\left(x+h\right)-f\left(x\right)}{h}{% endequation %}.

מושג הגבול מצריך הגדרה קפדנית בפני עצמו, וגם לו הקדשתי <a href="http://www.gadial.net/2010/10/03/limit_of_sequence/">פוסט</a>. בכל זאת צריך להזכיר את ההגדרה המדויקת: הפונקציה {% equation %}f:\mathbb{R}\to\mathbb{R}{% endequation %} מקיימת {% equation %}\lim_{x\to x_{0}}f\left(x\right)=L{% endequation %} אם לכל {% equation %}\varepsilon&gt;0{% endequation %} קיים {% equation %}\delta&gt;0{% endequation %} כך שאם {% equation %}\left|x-x_{0}\right|&lt;\delta{% endequation %} אז {% equation %}\left|f\left(x\right)-L\right|&lt;\varepsilon{% endequation %}. ועכשיו אנחנו צריכים לעצור ולשאול את עצמנו - מה בהגדרה הזו דורש את היות {% equation %}f{% endequation %} פונקציה שמוגדרת על מספרים ממשיים? מה צריך לתקן כדי להיות מסוגלים להכליל את ההגדרה לפונקציות מעל מרחבים אחרים? התשובה היא פשוטה - הערך המוחלט.

הערך המוחלט משמש בהגדרת הגבול בתור מקרה פרטי של <strong>פונקצית מרחק</strong>, (או בשם אחר <strong>מטריקה</strong>). את המושג הזה אפשר להציג בצורה כללית מאוד: אם {% equation %}A{% endequation %} היא קבוצה, אז מטריקה היא כל פונקציה {% equation %}d:A\times A\to\mathbb{R}{% endequation %} כך ש-{% equation %}d\left(x,y\right)=0{% endequation %} אם ורק אם {% equation %}x=y{% endequation %}, ו-{% equation %}d\left(x,y\right)=d\left(y,x\right){% endequation %} לכל {% equation %}x,y{% endequation %}, ו-{% equation %}d\left(x,y\right)\le d\left(x,z\right)+d\left(y,z\right){% endequation %} לכל {% equation %}x,y,z{% endequation %}. למה שלוש התכונות הללו דווקא? כי כשמסתכלים על מה שעושים בהוכחות שמערבות את מושג הגבול, אפשר לראות שאנחנו לא נזקקים לכל התכונות האפשריות של ערך מוחלט במהלך ההוכחה, ולעתים קרובות שלוש התכונות שציינתי מספיקות בהחלט כדי להשיג את אותן התוצאות.

לכן, השלב הראשון בהכללת מושג הנגזרת לפונקציות מרוכבות הוא הכללת מושג המרחק עבור מספרים מרוכבים. אבל זה קל - כבר ראינו איך מוגדר ערך מוחלט עבור מספרים מרוכבים: {% equation %}\left|a+bi\right|=\sqrt{a^{2}+b^{2}}{% endequation %}. זו אותה מטריקה בדיוק כמו המטריקה על {% equation %}\mathbb{R}^{2}{% endequation %} שבה משתמשים כשרוצים להגדיר חשבון דיפרנציאלי על פונקציות מ- ואל {% equation %}\mathbb{R}^{2}{% endequation %}. אז בעצם, מה ההבדל בין חשבון דיפרנציאלי של פונקציות {% equation %}f:\mathbb{R}^{2}\to\mathbb{R}^{2}{% endequation %} ובין פונקציות {% equation %}f:\mathbb{C}\to\mathbb{C}{% endequation %}? נדבר על זה עוד מעט.

אז יש לנו מושג של גבול של פונקציה מרוכבת (ובדומה גם אפשר להגדיר גבול של סדרה מרוכבת, אבל אין לנו צורך בגבולות כאלו עדיין). מכאן ההגדרה של נגזרת מרוכבת נובעת כמעט מעצמה: אם {% equation %}f:\mathbb{C}\to\mathbb{C}{% endequation %} היא פונקציה מרוכבת ו-{% equation %}z\in\mathbb{C}{% endequation %} הוא מספר מרוכב כלשהו, אז אנו מגדירים {% equation %}f^{\prime}\left(z_{0}\right)=\lim_{\Delta z\to0}\frac{f\left(z_{0}+\Delta z\right)-f\left(z_{0}\right)}{\Delta z}{% endequation %}. אם הגבול הזה קיים (ושונה מאינסוף), אומרים שהפונקציה <strong>גזירה</strong> בנקודה {% equation %}z_{0}{% endequation %}. זה הכל. אין כאן שום דבר חדש למי שכבר מכיר חדו"א; אבל כפי שנראה בקרוב, אם {% equation %}f:\mathbb{C}\to\mathbb{C}{% endequation %} היא גזירה, ההשלכות של זה הן קיצוניות יותר מאשר עבור פונקציה ממשית.

רגע, השלכות? אילו השלכות יכולות להיות לכך שפונקציה היא גזירה? ובכן, משפט בסיסי אחד בחדו"א הוא שכל פונקציה גזירה היא גם רציפה בכל נקודה שבה היא גזירה (רציפות פירושה ש-{% equation %}\lim_{x\to x_{0}}f\left(x\right)=f\left(x_{0}\right){% endequation %}). המשפט הזה תקף גם עבור פונקציות מרוכבות, וכפי שנראה, ההוכחה "אדישה" לשאלה אם הפונקציה מרוכבת או לא, כל עוד מושג הגבול שלנו מתנהג באותו האופן.

ההוכחה מתבססת על השוויון הבא: {% equation %}f\left(z_{0}+\Delta z\right)=f\left(z_{0}\right)+\frac{f\left(z_{0}+\Delta z\right)-f\left(z_{0}\right)}{\Delta z}\cdot\Delta z{% endequation %} - שהוא, כמובן, טריוויאלי. מה שמעניין הוא מה שקורה כאשר משאיפים את {% equation %}\Delta z{% endequation %} לאפס: מקבלים ש-

{% equation %}\lim_{\Delta z\to0}f\left(z_{0}+\Delta z\right)=\lim_{\Delta z\to0}\left(f\left(z_{0}\right)+\frac{f\left(z_{0}+\Delta z\right)-f\left(z_{0}\right)}{\Delta z}\cdot\Delta z\right)=f\left(z_{0}\right)+f^{\prime}\left(z_{0}\right)\cdot0=f\left(z_{0}\right){% endequation %}

כאשר השוויון האחרון נובע מכך ש-{% equation %}\lim_{\Delta z\to0}\frac{f\left(z_{0}+\Delta z\right)-f\left(z_{0}\right)}{\Delta z}=f^{\prime}\left(z_{0}\right){% endequation %} וזה מספר מרוכב, ואילו {% equation %}\lim_{\Delta z\to0}\Delta z=0{% endequation %}, וגבול של מכפלה של שני גבולות מתכנסים שווה למכפלה שלהם. רק כדי לשכנע אתכם סופית בכך שאין הבדל בין חדו"א רגיל ואנליזה מרוכבת בנקודה הזו, אני אחזור על איך מוכיחים את הטענה הזו. פורמלית אני רוצה להוכיח שאם {% equation %}\lim_{z\to z_{0}}f\left(z\right)=a{% endequation %} ו-{% equation %}\lim_{z\to z_{0}}g\left(z\right)=b{% endequation %} אז {% equation %}\lim_{z\to z_{0}}f\left(z\right)g\left(z\right)=ab{% endequation %}. כלומר, אני רוצה להיות מסוגל לחסום בצורה טובה את הביטוי {% equation %}\left|f\left(z\right)g\left(z\right)-ab\right|{% endequation %}. לשם כך, אני נוקט את התעלול הכי ישן בספר - מוסיף ומחסיר את אותו גורם, שאחרי טיפה משחקים אפשר לראות שכדאי שיהיה {% equation %}bf\left(z\right){% endequation %} כדי שנוכל לקבל חסם שכולל את שני הגבולות שאנחנו יודעים עליהם:

{% equation %}\left|f\left(z\right)g\left(z\right)-ab\right|=\left|f\left(z\right)g\left(z\right)+bf\left(z\right)-bf\left(z\right)-ab\right|=\left|f\left(z\right)\left[g\left(z\right)-b\right]+b\left[f\left(z\right)-a\right]\right|{% endequation %}

{% equation %}\le\left|f\left(z\right)\right|\left|g\left(z\right)-b\right|+\left|b\right|\left|f\left(z\right)-a\right|{% endequation %}

עכשיו, יהא {% equation %}\varepsilon&gt;0{% endequation %} כלשהו. אנחנו רוצים למצוא {% equation %}\delta{% endequation %} כך שלכל {% equation %}z{% endequation %} שמקיים {% equation %}\left|z-z_{0}\right|&lt;\delta{% endequation %}, מתקיים ש-{% equation %}\left|f\left(z\right)\right|\left|g\left(z\right)-b\right|+\left|b\right|\left|f\left(z\right)-a\right|&lt;\varepsilon{% endequation %}. ראשית, מכיוון ש-{% equation %}\lim_{z\to z_{0}}f\left(z\right)=a{% endequation %} נובע מכך שקיים {% equation %}\delta_{1}{% endequation %} כך שאם {% equation %}\left|z-z_{0}\right|&lt;\delta_{1}{% endequation %} אז {% equation %}\left|f\left(z\right)-a\right|&lt;\frac{\varepsilon}{2\left|b\right|}{% endequation %}, ולכן {% equation %}\left|b\right|\left|f\left(z\right)-a\right|&lt;\frac{\varepsilon}{2}{% endequation %}.

שנית, קיים {% equation %}\delta_{2}{% endequation %} כך שאם {% equation %}\left|z-z_{0}\right|&lt;\delta_{2}{% endequation %} אז {% equation %}\left|f\left(z\right)-a\right|&lt;1{% endequation %}, ולכן {% equation %}\left|f\left(z\right)\right|&lt;1+a{% endequation %}. הויסה, רגע, רגע! איך עשיתי את זה? ובכן, תכונה כללית של ערך מוחלט: {% equation %}\left|x-y\right|\ge\left|x\right|-\left|y\right|{% endequation %}. איך מוכיחים אותה? ובכן, {% equation %}\left|x\right|=\left|x-y+y\right|\le\left|x-y\right|+\left|y\right|{% endequation %}. כל מה שאני מתבסס עליו הוא אי-שוויון המשולש (והטריק הרגיל של לחסר ולחבר את אותו הדבר).

כעת, קיים גם {% equation %}\delta_{3}{% endequation %} כך שאם {% equation %}\left|z-z_{0}\right|&lt;\delta_{3}{% endequation %} אז {% equation %}\left|g\left(z\right)-b\right|&lt;\frac{\varepsilon}{2\left(1+a\right)}{% endequation %}, ולכן אם {% equation %}\left|z-z_{0}\right|&lt;\min\left\{ \delta_{2},\delta_{3}\right\} {% endequation %} מתקיים {% equation %}\left|f\left(z\right)\right|\left|g\left(z\right)-b\right|&lt;\left(1+a\right)\frac{\varepsilon}{2\left(1+a\right)}=\frac{\varepsilon}{2}{% endequation %}. המסקנה הסופית: נגדיר {% equation %}\delta=\min\left\{ \delta_{1},\delta_{2},\delta_{3}\right\} {% endequation %} ונקבל שאם {% equation %}\left|z-z_{0}\right|&lt;\delta{% endequation %} אז

{% equation %}\left|f\left(z\right)\right|\left|g\left(z\right)-b\right|+\left|b\right|\left|f\left(z\right)-a\right|&lt;\frac{\varepsilon}{2}+\frac{\varepsilon}{2}=\varepsilon{% endequation %}

שימו לב בכמה מעט השתמשנו בהוכחה הזו.

חזרה לענייננו. הוכחנו שפונקציה גזירה היא גם רציפה; בואו נראה עוד כמה תכונות בסיסיות של נגזרות. תכונה נחמדה אחת של נגזרת היא שמדובר על אופרטור <strong>לינארי</strong> - זה אומר שאם {% equation %}a,b\in\mathbb{C}{% endequation %} ו-{% equation %}f,g{% endequation %} הן פונקציות מרוכבות, אז {% equation %}\left[af+bg\right]^{\prime}=af^{\prime}+bg^{\prime}{% endequation %} (למי שמכיר אלגברה לינארית - זה אומר שאופרטור הגזירה הוא טרנספורמציה לינארית, עבור מרחבים וקטוריים מתאימים של פונקציות). ההוכחה לזה נובעת מייד מתכונות של גבולות ושימוש בהגדרה של נגזרת ולא אכנס אליה. תחת זאת אציג את ההוכחה למשהו טיפה יותר מסובך - נוסחת הנגזרת של מכפלה, שזהה גם היא למקרה הממשי: {% equation %}\left[fg\right]^{\prime}=f^{\prime}g+fg^{\prime}{% endequation %}. ההוכחה, כרגיל, מבוססת על לחבר ולהחסיר את אותו דבר:

{% equation %}\left[fg\right]^{\prime}\left(z_{0}\right)=\lim_{\Delta z\to0}\frac{fg\left(z_{0}+\Delta z\right)-fg\left(z_{0}\right)}{\Delta z}=\lim_{\Delta z\to0}\frac{fg\left(z_{0}+\Delta z\right)+f\left(z_{0}+\Delta z\right)g\left(z_{0}\right)-f\left(z_{0}+\Delta z\right)g\left(z_{0}\right)-fg\left(z_{0}\right)}{\Delta z}{% endequation %}

{% equation %}=\lim_{\Delta z\to0}\frac{f\left(z_{0}+\Delta z\right)\left[g\left(z_{0}+\Delta z\right)-g\left(z_{0}\right)\right]}{\Delta z}+\lim_{\Delta z\to0}\frac{g\left(z_{0}\right)\left[f\left(z_{0}+\Delta z\right)-f\left(z_{0}\right)\right]}{\Delta z}{% endequation %}

{% equation %}=f\left(z_{0}\right)g^{\prime}\left(z_{0}\right)+g\left(z_{0}\right)f^{\prime}\left(z_{0}\right){% endequation %}

הבנתם את הפרינציפ. זה מה שתמיד כיף בהכללות מתמטיות - האופן שבו חלק מההוכחות פשוט ממשיכות לעבוד למרות ששינינו לגמרי את "שדה המשחק" שלהן.

ומה עם גזירה של פונקציות קונקרטיות? ובכן, בינתיים מה שפשוט להציג הוא את הגזירה של פולינום. פולינום הוא ביטוי מהצורה {% equation %}\sum a_{n}z^{n}{% endequation %}, ולכן אפשר להשתמש בלינאריות של הנגזרת כדי לקבל ש-{% equation %}\left[\sum a_{n}z^{n}\right]^{\prime}=\sum a_{n}\left[z^{n}\right]^{\prime}{% endequation %}, כלומר די למצוא את הנגזרת של פונקציות מהצורה {% equation %}f\left(z\right)=z^{n}{% endequation %}. פונקציות כאלו אפשר להציג אינדוקטיבית בתור {% equation %}z^{n}=z^{n-1}\cdot z{% endequation %} ואז לגזור עם כלל הגזירה של מכפלה. בשביל הבסיס נצטרך להבין את הנגזרת של {% equation %}f\left(z\right)=z{% endequation %}, ואת זה אפשר לעשות ישירות מההגדרה:

{% equation %}f^{\prime}\left(z_{0}\right)=\lim_{\Delta z\to0}\frac{f\left(z_{0}+\Delta z\right)-f\left(z_{0}\right)}{\Delta z}=\lim_{\Delta z\to0}\frac{z_{0}+\Delta z-z_{0}}{\Delta z}=\lim_{\Delta z\to0}1=1{% endequation %}

וכעת אפשר לנחש (אחרי שמנסים כמה מקרים פרטיים, או סתם לזכור מה קורה במספרים ממשיים) ש-{% equation %}\left[z^{n}\right]^{\prime}=nz^{n-1}{% endequation %}, ולהוכיח את זה באינדוקציה:

{% equation %}\left[z^{n}\right]^{\prime}=\left[z^{n-1}\right]^{\prime}z+z^{n-1}=\left(n-1\right)z^{n-2}\cdot z+z^{n-1}=nz^{n-1}{% endequation %}

טוב, מספיק עם זה. עד עכשיו כל מה שעשיתי הוא לקחת תוצאות מחדו"א במספרים ממשיים ולהגיד "היי, תראו, איזה מגניב, זה עובד גם כאן!". עד כאן. אני רוצה להראות משהו חדש - את <strong>משוואות קושי-רימן</strong>. נתחיל דווקא בלדבר על פונקציות ממשיות מהמרחב לעצמו, דהיינו {% equation %}f:\mathbb{R}^{2}\to\mathbb{R}^{2}{% endequation %}. איך אפשר להגדיר נגזרת של פונקציה שכזו? אפשר לדבר על גבולות ב-{% equation %}\mathbb{R}^{2}{% endequation %} - כבר אמרנו שיש לנו על {% equation %}\mathbb{R}^{2}{% endequation %} את אותה מטריקה כמו ב-{% equation %}\mathbb{C}{% endequation %}, אבל משהו אחר ישתבש. אם ננסה להגדיר {% equation %}f^{\prime}\left(a_{0}\right)=\lim_{\Delta a\to0}\frac{f\left(a+\Delta a\right)-f\left(a\right)}{\Delta a}{% endequation %} נקבל משהו שהוא ביטוי חסר משמעות, כי יש בו שבר שבו במונה ובמכנה יש איברים של {% equation %}\mathbb{R}^{2}{% endequation %}, כלומר אנחנו מחלקים איבר של {% equation %}\mathbb{R}^{2}{% endequation %} באיבר אחר של {% equation %}\mathbb{R}^{2}{% endequation %}. אבל על {% equation %}\mathbb{R}^{2}{% endequation %} אין לנו מושג של חילוק - {% equation %}\mathbb{R}^{2}{% endequation %} אינו <strong>שדה</strong>. אם אתם זוכרים, <a href="http://www.gadial.net/2013/07/21/complex_analysis_intro/">בפוסט הראשון</a> על פונקציות מרוכבות התייחסתי לנקודה הזו. המספרים המרוכבים הם כן שדה בזכות פעולת כפל "מתוחכמת" (שממנה נובעת פעולת החילוק). הנה הנקודה המדוייקת שבו האנליזה של {% equation %}\mathbb{R}^{2}{% endequation %} נפרדת מהאנליזה המרוכבת.

אבל מה כן עושים ב-{% equation %}\mathbb{R}^{2}{% endequation %}? דרך אחת לתאר פונקציות כאלו היא בתור זוג פונקציות {% equation %}u,v:\mathbb{R}^{2}\to\mathbb{R}{% endequation %} שמקבלות כל אחת זוג ערכים ומחזירות ערך בודד: {% equation %}f\left(x,y\right)=\left(u\left(x,y\right),v\left(x,y\right)\right){% endequation %}. כעת אפשר לדבר על הנגזרות של כל פונקציה כזו בנפרד. אבל מה המשמעות של נגזרת של פונקציה בשני משתנים? חשבו על הפונקציה כאילו היא מתארת קווי גובה של הר - לכל נקודה במישור מותאם ה"גובה" שלה. אז נגזרת של הפונקציה היא <strong>שיפוע</strong> ההר בנקודה מסויימת; אבל הכרחי לשאול - שיפוע ביחס לאיזה כיוון? חשבו על שפת תהום, שבה בכיוון אחד יש לנו נפילה בכיוון אנכי ובכיוון אחר יש לנו משטח אופקי...

שני הכיוונים ה"נאיביים" הם אלו של ציר {% equation %}x{% endequation %} וציר {% equation %}y{% endequation %}. עבורם פשוט נוהגים באופן הבא: "מקפיאים" את אחד המשתנים, וגוזרים לפי המשתנה השני. מה שמתקבל נקרא <strong>נגזרת חלקית</strong>. למשל:

{% equation %}\frac{\partial u}{\partial x}\left(x,y\right)=\lim_{\Delta x\to0}\frac{u\left(x+\Delta x,y\right)-u\left(x,y\right)}{\Delta x}{% endequation %}

{% equation %}\frac{\partial u}{\partial y}\left(x,y\right)=\lim_{\Delta y\to0}\frac{u\left(x,y+\Delta y\right)-u\left(x,y\right)}{\Delta y}{% endequation %}

כאשר כאן {% equation %}a,b\in\mathbb{R}{% endequation %}. הסימון {% equation %}\frac{\partial u}{\partial x}{% endequation %} לתיאור נגזרת חלקית הוא וריאציה על הסימון {% equation %}\frac{du}{dx}{% endequation %} לתיאור נגזרת של פונקציה במשתנה יחיד (ה-{% equation %}\partial{% endequation %} הוא מין {% equation %}d{% endequation %} מסולסלת).

מסתבר ששתי הנגזרות החלקיות הללו מספיקות לנו כדי למצוא את הנגזרת של הפונקציה בכל כיוון, אבל אני לא מדבר כאן על אנליזה ממשית אז נעזוב את זה לבינתיים. תחת זאת אני רוצה לשאול את השאלה - מה קורה כאשר מנסים לנתח פונקציה מרוכבת בגישת הנגזרות החלקיות הזו?

ובכן, תהא {% equation %}f:\mathbb{C}\to\mathbb{C}{% endequation %} פונקציה מרוכבת. אפשר להציג אותה בתור זוג של פונקציות ממשיות {% equation %}u,v:\mathbb{R}^{2}\to\mathbb{R}{% endequation %}: {% equation %}f\left(x+yi\right)=u\left(x,y\right)+iv\left(x,y\right){% endequation %}. עכשיו, נרצה לחשב את הנגזרת של {% equation %}f{% endequation %} בנקודה {% equation %}z=x+iy{% endequation %} <strong>בשתי דרכים שונות</strong>. בואו נסתכל קודם כל על הגבול הבא:

{% equation %}\lim_{\Delta x\to0}\frac{f\left(z+\Delta x\right)-f\left(z\right)}{\Delta x}{% endequation %}

כאשר {% equation %}\Delta x\in\mathbb{R}{% endequation %}. הגבול הזה הוא מעין גרסה מצומצמת של הגבול ה"כללי", שבו מה ששואף לאפס יכול להיות מספר מרוכב כלשהו ולא רק מספר ממשי. אם הגבול ה"כללי" קיים, אז בפרט הגבול ה"פרטי" קיים ושווה לו (תרגיל קל למדי להוכחה - עבור אפסילון נתון זו אותה הדלתא!). מצד שני, אם נעבור להציג את {% equation %}f{% endequation %} בעזרת הפונקציות הממשיות, נקבל:

{% equation %}f^{\prime}\left(z\right)=\lim_{\Delta x\to0}\frac{u\left(x+\Delta x,y\right)-u\left(x,y\right)}{\Delta x}+\lim_{\Delta x\to0}i\frac{v\left(x+\Delta x,y\right)-v\left(x,y\right)}{\Delta x}=\frac{\partial u}{\partial x}\left(x,y\right)+i\frac{\partial v}{\partial x}\left(x,y\right){% endequation %}

עד כאן, מתבקש; אבל עכשיו בואו נחשב את הגבול לא לאורך ציר {% equation %}x{% endequation %} אלא לאורך ציר {% equation %}y{% endequation %}: נחשב את הגבול

{% equation %}\lim_{\Delta y\to0}\frac{f\left(z+i\Delta y\right)-f\left(z\right)}{i\Delta y}{% endequation %}

כאשר {% equation %}\Delta y\in\mathbb{R}{% endequation %}.

תזכרו מה זה אומר לחלק ב-{% equation %}i{% endequation %}: מכיוון ש-{% equation %}i^{4}=1{% endequation %} אז {% equation %}\frac{1}{i}=i^{3}{% endequation %}, ומצד שני {% equation %}i^{3}=i^{2}i=-i{% endequation %}. לכן לחלק ב-{% equation %}i{% endequation %} זה בעצם לכפול ב-{% equation %}-i{% endequation %}. מכאן שנקבל:

נקבל:

{% equation %}f^{\prime}\left(z\right)=\lim_{\Delta y\to0}\frac{u\left(x,y+\Delta y\right)-u\left(x,y\right)}{i\Delta y}+\lim_{\Delta x\to0}i\frac{v\left(x,y+\Delta y\right)-v\left(x,y\right)}{i\Delta y}=-i\frac{\partial u}{\partial y}\left(x,y\right)+\frac{\partial v}{\partial y}\left(x,y\right){% endequation %}

כלומר, דווקא {% equation %}u{% endequation %} (החלק ה"ממשי") הוכפל בסופו של דבר ב-{% equation %}-i{% endequation %}, ואילו {% equation %}v{% endequation %} בסוף יצא עם מקדם 1, בלי {% equation %}i{% endequation %} ובלי מינוס ובלי שום דבר.

עכשיו אפשר להשוות את שני הערכים שקיבלנו:

{% equation %}\frac{\partial u}{\partial x}\left(x,y\right)+i\frac{\partial v}{\partial x}\left(x,y\right)=\frac{\partial v}{\partial y}\left(x,y\right)-i\frac{\partial u}{\partial y}\left(x,y\right){% endequation %}

כשמשווים שני מספרים מרוכבים, הם שווים רק אם החלקים הממשיים והמדומים שלהם שווים, ולכן נקבל בעצם <strong>זוג</strong> של משוואות:

{% equation %}\frac{\partial u}{\partial x}=\frac{\partial v}{\partial y}{% endequation %}

{% equation %}\frac{\partial u}{\partial y}=-\frac{\partial v}{\partial x}{% endequation %}

שמתקיימות בכל נקודה שבה {% equation %}f{% endequation %} גזירה. המשוואות הללו נקראות <strong>משוואות קושי-רימן</strong>.

משוואות קושי רימן מראות שאם אנחנו רוצים לבנות פונקציה מרוכבת גזירה, אי אפשר סתם לקחת שתי פונקציות {% equation %}u,v{% endequation %} ולחבר אותן ביחד, אפילו אם שתיהן גזירות בעצמן (כלומר, אם יש להן נגזרות חלקיות). הפונקציות הללו חייבות לקיים קשר כלשהו בין הנגזרות החלקיות שלהן כדי שהפונקציה המרוכבת שתתקבל מהן תהיה גזירה (ואם הייתי רוצה לקלל, הייתי קורא לקשר הזה "משוואה דיפרנציאלית חלקית"). אבל הקשר הזה בין שתי הפונקציות גם מצביע על עוד תכונה שכל פונקציה לבדה חייבת לקיים - בואו ניקח את {% equation %}u{% endequation %} ונגזור את הנגזרות החלקיות שלה שוב (צריך להסביר למה שהנגזרות החלקיות יהיו גזירות שוב - בינתיים בואו רק תניחו שזה קורה). נקבל:

{% equation %}\frac{\partial^{2}u}{\partial x^{2}}=\frac{\partial v}{\partial x\partial y}{% endequation %}

{% equation %}\frac{\partial^{2}u}{\partial y^{2}}=-\frac{\partial v}{\partial y\partial x}{% endequation %}

{% equation %}\frac{\partial v}{\partial x\partial y}{% endequation %} הוא מה שמקבלים כשגוזרים את {% equation %}v{% endequation %} קודם על פי {% equation %}x{% endequation %} ואז על פי {% equation %}y{% endequation %} ו-{% equation %}\frac{\partial v}{\partial y\partial x}{% endequation %} הוא מה שקורה כשגוזרים על פי הסדר ההפוך. יש משפט באנליזה שמראה שאם הנגזרות ה"מעורבות" הללו רציפות אז הן שוות, כלומר {% equation %}\frac{\partial v}{\partial y\partial x}=\frac{\partial v}{\partial x\partial y}{% endequation %}; המסקנה היא שבמקרה שלנו {% equation %}\frac{\partial^{2}u}{\partial x^{2}}+\frac{\partial^{2}u}{\partial y^{2}}=0{% endequation %}. בניסוח אחר, {% equation %}u{% endequation %} היא פונקציה שמתאפסת על ידי אופרטור ה<strong>לפליסאן</strong>, {% equation %}\Delta=\frac{\partial^{2}}{\partial x^{2}}+\frac{\partial^{2}}{\partial y^{2}}{% endequation %}. לפונקציות כאלו יש שם מיוחד - פונקציות <strong>הרמוניות</strong>. אני לא נכנס עכשיו לפרטים של מה זה בדיוק אומר; אני רק רוצה שנקבל תחושה של איך שמשוואות קושי רימן מצביעות על כך שלא כל פונקציה מהרחוב יכולה להשתתף בפרוייקט הכביר והנשגב של בניית פונקציה מרוכבת גזירה: יש תנאים לא טריוויאליים שצריכים להתקיים.

עכשיו אני רוצה להכניס לתמונה מושג שעד כה החבאתי - <strong>פונקציה אנליטית</strong>. למשמעות המלאה של המושג הזה נגיע רק בהמשך, אז בינתיים אתן הגדרה יבשה למדי - אם {% equation %}D{% endequation %} היא קבוצה פתוחה במישור המרוכב - מה שאקרא לו גם "תחום" - אז פונקציה מרוכבת {% equation %}f:D\to\mathbb{C}{% endequation %} היא <strong>אנליטית</strong> אם היא גזירה בכל נקודה של {% equation %}D{% endequation %} (אם תחום ההגדרה של {% equation %}f{% endequation %} רחב יותר אפשר להצטמצמם רק ל-{% equation %}D{% endequation %} ולומר ש-"{% equation %}f{% endequation %} אנליטית על {% equation %}D{% endequation %}"). שימו לב שאנליטיות היא לא תכונה נקודתית - היא תכונה שמתארת את התנהגות הפונקציה בתוך קבוצה פתוחה. מה זו קבוצה פתוחה? בהקשר של המישור המרוכב, זוהי קבוצה שכל נקודה בה היא נקודה פנימית של הקבוצה: לכל {% equation %}z_{0}\in D{% endequation %} קיים {% equation %}r&gt;0{% endequation %} ממשי כך שאם {% equation %}\left|z-z_{0}\right|&lt;r{% endequation %} אז {% equation %}z\in D{% endequation %} (ציורית, כל נקודה {% equation %}z_{0}{% endequation %} בקבוצה ניתן להקיף בעיגול קטן שכולו מוכל בקבוצה). למה חשוב לנו ש-{% equation %}D{% endequation %} תהיה פתוחה? נראה זאת בהמשך; אנליטיות של פונקציה נותנת לנו "קצת יותר" מאשר גזירות בלבד.

עכשיו אני רוצה לתאר בנפנוף ידיים את הכיוון השני של המשפט על נוסחאות קושי-רימן: לא רק שמדובר על תנאי <strong>הכרחי</strong> עבור פונקציות כדי שיוכלו להרכיב פונקציה אנליטית, זה גם תנאי <strong>מספיק</strong>: אם {% equation %}u,v{% endequation %} הן בעלות נגזרות חלקיות רציפות שמקיימות את משוואות קושי רימן על תחום {% equation %}D{% endequation %} כלשהו, אז {% equation %}u+iv{% endequation %} היא פונקציה אנליטית.

ההוכחה לא מסובכת, אבל מתבססת על עוד משהו באנליזה "רגילה" שלא הראיתי אף פעם - פיתוח טיילור של פונקציה בשני משתנים. בקצרה, אפשר לכתוב את הערך של {% equation %}u{% endequation %} אחרי שמזיזים טיפה את הערכים שלה ביחס לנקודה {% equation %}\left(x,y\right){% endequation %} נתונה על ידי הערך שלה ב-{% equation %}\left(x,y\right){% endequation %}, הערכים של הנגזרות החלקיות הראשונות שלה ב-{% equation %}\left(x,y\right){% endequation %}, ועוד שארית "קטנה". זה מתואר על ידי הנוסחה המזעזעת הבאה:

{% equation %}u\left(x+\Delta x,y+\Delta y\right)=u\left(x,y\right)+\frac{\partial u}{\partial x}\left(x,y\right)\Delta x+\frac{\partial u}{\partial y}\left(x,y\right)\Delta y+R\left(\Delta x,\Delta y\right){% endequation %}

כאשר {% equation %}R\left(\Delta x,\Delta y\right){% endequation %} היא "קטנה", במובן זה שאם נסמן {% equation %}\Delta z=\Delta x+i\Delta y{% endequation %} נקבל ש-{% equation %}\lim_{\Delta z\to0}\frac{R\left(\Delta x,\Delta y\right)}{\left|\Delta z\right|}=0{% endequation %}. באותו אופן אפשר לכתוב עבור {% equation %}v{% endequation %}:

{% equation %}v\left(x+\Delta x,y+\Delta y\right)=v\left(x,y\right)+\frac{\partial v}{\partial x}\left(x,y\right)\Delta x+\frac{\partial v}{\partial y}\left(x,y\right)\Delta y+S\left(\Delta x,\Delta y\right){% endequation %}

ועכשיו, אם נכתוב את {% equation %}f\left(z+\Delta z\right)=u\left(x+\Delta x,y+\Delta y\right)+iv\left(x+\Delta x,y+\Delta y\right){% endequation %} במפורש על פי הנוסחאות שלמעלה <strong>ונשתמש בנוסחאות קושי רימן</strong>, העסק המזוויע הזה יצטמצם למשהו שדי קל להבין:

{% equation %}f\left(z+\Delta z\right)=f\left(z\right)+\left(\frac{\partial u}{\partial x}\left(x,y\right)+i\frac{\partial v}{\partial x}\left(x,y\right)\right)\Delta z+R\left(\Delta z\right)+iS\left(\Delta z\right){% endequation %}

עכשיו קחו את האיבר הראשון באגף ימין, חסרו אותו משני האגפים, חלקו אותם ב-{% equation %}\Delta z{% endequation %}, והופס:

{% equation %}\frac{f\left(z+\Delta z\right)-f\left(z\right)}{\Delta z}=\left(\frac{\partial u}{\partial x}\left(x,y\right)+i\frac{\partial v}{\partial x}\left(x,y\right)\right)+\frac{R\left(\Delta z\right)+iS\left(\Delta z\right)}{\Delta z}{% endequation %}

ואחרי השאפת {% equation %}\Delta z{% endequation %} לאפס נישאר עם {% equation %}f^{\prime}\left(z\right)=\frac{\partial u}{\partial x}\left(x,y\right)+i\frac{\partial v}{\partial x}\left(x,y\right){% endequation %} . קיבלנו ש-{% equation %}f{% endequation %} גזירה וגם מצאנו נוסחה לנגזרת שלה.

בואו נראה דוגמה קלילה לסיום, כי בלי זה באמת אי אפשר. כזכור, הגדרנו את פונקצית האקספוננט (על התחום {% equation %}\mathbb{C}{% endequation %}) באופן הבא: {% equation %}e^{x+iy}=e^{x}\cos y+ie^{x}\sin y{% endequation %}. כלומר, {% equation %}u\left(x,y\right)=e^{x}\cos y{% endequation %} ו-{% equation %}u\left(x,y\right)=e^{x}\sin y{% endequation %} במקרה שלנו. בואו נחשב את הנגזרות החלקיות:

{% equation %}\frac{\partial u}{\partial x}=e^{x}\cos y{% endequation %}

{% equation %}\frac{\partial u}{\partial y}=-e^{x}\sin y{% endequation %}

{% equation %}\frac{\partial v}{\partial x}=e^{x}\sin y{% endequation %}

{% equation %}\frac{\partial v}{\partial y}=e^{x}\cos y{% endequation %}

ובבירור משוואות קושי רימן אכן מתקיימות. במובן מסויים פונקציית האקספוננט גם מקיימת את המשוואות הללו בצורה "טבעית" מאוד לטעמי, אבל לא אנסה לשכנע אתכם בכך.

לסיכום, משוואות קושי-רימן הן הצצה ראשונה לאופן שבו תכונות כמו גזירות הן בעלות רמת סיבוכיות נוספת לעומת מה שקורה בפונקציות ממשיות, אבל זה רק החימום - תאמינו לי שבהמשך הולכים לקרות דברים מוזרים הרבה יותר.
