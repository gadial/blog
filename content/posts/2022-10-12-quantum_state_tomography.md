---
title: "טומוגרפיה קוונטית: איך מגלים מה כבר יש לנו?"
layout: post
categories:
  - חישוב קוונטי
tags:
  - טומוגרפיה קוונטית
description: "אמרתי כל הזמן שמדידה של מצב קוונטי הורסת אותו ואי אפשר יותר לדעת מה הוא היה, ולכן אי אפשר לחשב את האמפליטודות של המצב על ידי מדידה שלו. ובכן, אז אמרתי."
image: "2022/qst.png"
---

<a href="https://gadial.net/2022/10/09/density_matrices/">בפוסט הקודם שלי</a> הצגתי את מה שקראתי לו "פורמליזם מטריצת הצפיפות" ולפני שאני ממשיך לדבר עליו - ספציפית, על השינויים שהוא יכול לעבור - אני רוצה לעצור ולהציג נושא שישתמש באופן ישיר בפורמליזם הזה והוא די מגניב בזכות עצמו: טומוגרפיית מצבים קוונטית (Quantum State Tomography).

דבר אחד שאני מקווה שהדגשתי בסדרת הפוסטים עד כה הוא שמדידה של מצב קוונטי <strong>הורסת</strong> את המצב הקוונטי. משמידה אותו. חורבן. הרס. אם הייתי במצב {% equation %}\left|+\right\rangle {% endequation %} ומדדתי מדידה "רגילה", בבסיס {% equation %}Z{% endequation %} (כלומר, מדידה שמתאימה לאיברים {% equation %}\left\{ \left|0\right\rangle ,\left|1\right\rangle \right\} {% endequation %}), אז זהו, אני כבר לא ב-{% equation %}\left|+\right\rangle {% endequation %}. אני או ב-{% equation %}\left|0\right\rangle {% endequation %} או ב-{% equation %}\left|1\right\rangle {% endequation %}. אם הייתי במצב כללי {% equation %}\alpha\left|0\right\rangle +\beta\left|1\right\rangle {% endequation %} ומדדתי בבסיס {% equation %}Z{% endequation %} , אז זהו. אני או ב-{% equation %}\left|0\right\rangle {% endequation %} או ב-{% equation %}\left|1\right\rangle {% endequation %} וזהו. המקדמים {% equation %}\alpha,\beta{% endequation %} נעלמו ואינם עוד.

גרוע מכך - מדידה אחת פשוט <strong>לא יכולה</strong> ללמד אותי מהם {% equation %}\alpha,\beta{% endequation %}. אם קיבלתי {% equation %}\left|0\right\rangle {% endequation %} אני יכול לדעת ש-{% equation %}\alpha\ne0{% endequation %} אבל לא יותר מכך. באלגוריתמים הקוונטיים שהצגתי עד כה, כולל האלגוריתם של שור, לא התעניינו בערכים של האמפליטודות; רק ניסינו לבצע עליהם מניפולציות כדי להבטיח שבהסתברות גבוהה התוצאה הסופית תהיה כזו שעוזרת לנו.

אבל העניין הוא... שקצת שיקרתי. בהחלט <strong>אפשר</strong> לחשב את ה-{% equation %}\alpha,\beta{% endequation %} הללו מתוך המצב הקוונטי, וזאת בתנאי שיש לנו <strong>מספר עותקים שלו</strong>. כמה עותקים בדיוק - את זה נראה בקרוב. עכשיו, אפשר לטעון ובצדק שאי אפשר לשכפל מצב קוונטי (יש משפט כזה! No Cloning Theorem!) ולכן אני לא יכול סתם לקחת מצב קוונטי, לשכפל אותו ואז להשתמש בשיטה הקסומה שאני הולך להציג פה. זה נכון לגמרי; אבל אם המצב הקוונטי נוצר כתוצאה של תהליך מסוים, אני יכול לחזור על התהליך הזה שוב ושוב ולקבל את אותו מצב שוב ושוב. זה מה שהרצה פרקטית של אלגוריתם במחשב קוונטי עושה גם ככה: מריצה את אותו אלגוריתם מספר פעמים גדול (נאמר, 1,000?) על המחשב ויוצרת סטטיסטיקה של תוצאות.

כמובן, אפשר לשאול ובצדק - אם אנחנו אלו שמייצרים את המצב, האם זה לא אומר שאנחנו יודעים לאיזה מצב הגענו? ובכן, <strong>לא!</strong> משתי סיבות. ראשית, כי אני לא מניח שאנחנו יודעים לחשב מה המצב גם אם יש לנו מעגל קונקרטי שמייצר אותו - אולי החישוב המלא של מה שהמעגל עושה הוא מסובך? אולי יש בתוך המעגל אלמנטים שאנחנו יכולים לשלוט עליהם אבל אנחנו לא יודעים מה הם בדיוק עושים? ושנית, באופן די דומה למה שכבר אמרתי, במעגלים קוונטיים יש בעיה של <strong>רעשים</strong> והתנהגויות לא צפויות. ייתכן שאנחנו <strong>חושבים</strong>~שאנחנו מייצרים את {% equation %}\left|+\right\rangle {% endequation %} אבל עקב שגיאות במימוש של המחשב הקוונטי אנחנו תמיד מקבלים את {% equation %}\left|-\right\rangle {% endequation %} - זה <strong>בהחלט</strong> משהו שהיינו רוצים להיות מסוגלים לזהות. בפועל, זה אכן שימוש מרכזי של טומוגרפיה קוונטית - בדיקה שהמחשב אכן מתנהג כפי שאנו מצפים שיתנהג, והערכה של רמת הרעש שיש בו.

אם כן, הבה ונאמר שיש לנו מצב קוונטי ואנחנו מסוגלים לשחזר שוב ושוב במדויק את התהליך שיוצר אותו. ואנחנו מודדים אותו 1,000 פעם בבסיס {% equation %}Z{% endequation %} ומקבלים 483 פעם "0" ו-517 פעם "1". מה זה אומר על המצב שבו אני נמצא? אם אני ב-{% equation %}\left|+\right\rangle =\frac{\left|0\right\rangle +\left|1\right\rangle }{\sqrt{2}}{% endequation %} ומודד 1,000 פעמים בהחלט ייתכן שאקבל את התפלגות התוצאות הזו, אבל גם אם אני במצב {% equation %}\sqrt{\frac{483}{1000}}\left|0\right\rangle +\sqrt{\frac{517}{1000}}\left|1\right\rangle {% endequation %} זה ייתכן. כלומר, יש לנו בעיה כבר עם עצם זה שלחזור שוב ושוב על אותו ניסוי ולספור תוצאות לא נותן לנו את ההסתברויות שהובילו אליהן. אבל זו אפילו לא הבעיה המרכזית לבינתיים! 

אז בואו נניח לצורך הדיון שאיכשהו המדידות שלי מושלמות ואני מצליח לגלות בצורה מדויקת את ההסתברויות לכל התוצאות, כלומר אם המצב שלי הוא {% equation %}\left|+\right\rangle {% endequation %} אני מקבל את וקטור ההסתברויות {% equation %}\overline{p}=\left(\begin{array}{c} 0.5\\ 0.5 \end{array}\right){% endequation %}. מה הבעיה כאן? שגם אם המצב שלי הוא {% equation %}\left|-\right\rangle {% endequation %} אני אקבל את <strong>אותו וקטור הסתברויות בדיוק</strong>. מדידה בבסיס {% equation %}Z{% endequation %} פשוט <strong>לא מסוגלת</strong> להבדיל בין שני המצבים הללו. אני אקבל את אותה סטטיסטיקה בדיוק. אז מה עושים?

למרבה המזל, יש עוד מדידות בעולם חוץ ממדידה בבסיס {% equation %}Z{% endequation %}. למשל, מדידה בבסיס {% equation %}X{% endequation %}, שאבריה הם {% equation %}\left\{ \left|+\right\rangle ,\left|-\right\rangle \right\} {% endequation %}. מדידה כזו בוודאי יכולה להפריד בין {% equation %}\left|+\right\rangle {% endequation %} (שיחזיר וקטור הסתברויות {% equation %}\left(\begin{array}{c} 1\\ 0 \end{array}\right){% endequation %}) ובין {% equation %}\left|-\right\rangle {% endequation %} (שיחזיר וקטור הסתברויות {% equation %}\left(\begin{array}{c} 0\\ 1 \end{array}\right){% endequation %}). אלא מה? מדידה בבסיס {% equation %}X{% endequation %} לא מסוגלת להבדיל בין {% equation %}\left|0\right\rangle ,\left|1\right\rangle {% endequation %} ששניהם מחזירים {% equation %}\overline{p}=\left(\begin{array}{c} 0.5\\ 0.5 \end{array}\right){% endequation %} - אותה בעיה כמו קודם.

האם צריך להתייאש? בוודאי שלא! המסקנה צריכה להיות חיובית - אולי בסיס מדידה אחד הוא לא הפתרון, אבל שילוב של מידע מכמה מדידות שונות יאפשר לשחזר את המצב בודאות. מכאן מגיע השם של השיטה שאציג - <strong>טומוגרפיה קוונטית</strong>. בעולם האמיתי, "טומוגרפיה" הוא שם של טכניקה בתחומים רבים ושונים שמאפשרת לשחזר מידע על אובייקט מורכב (חומרים, איברים בגוף וכו') על ידי מדידה של "חתכים" שלו. כאן צריך לחשוב על מדידה בבסיס ספציפי (שנותנת הסתברויות) בתור "חתך" שכזה. אבל כמה חתכים צריך? כמה מידע צריך לשחזר?

בואו נסבך קצת יותר את הסיטואציה. מה אם התהליך שמייצר את המצב הקוונטי שלנו איננו דטרמיניסטי, למרות שהוא בעל חוקיות ברורה? למשל: התהליך קודם מייצר את המצב {% equation %}\left|+\right\rangle {% endequation %}, ואז התהליך עצמו מודד אותו בבסיס {% equation %}Z{% endequation %} וכמובן שלא מספר לנו מה התוצאה. זה אומר שהמצב הקוונטי שאנחנו מנסים לבצע לו טומוגרפיה הוא {% equation %}\left|0\right\rangle {% endequation %} בהסתברות {% equation %}\frac{1}{2}{% endequation %} ו-{% equation %}\left|1\right\rangle {% endequation %} בהסתברות {% equation %}\frac{1}{2}{% endequation %}. מדידה בבסיס {% equation %}Z{% endequation %} תיתן לנו את וקטור ההסתברויות {% equation %}\left(\begin{array}{c} 0.5\\ 0.5 \end{array}\right){% endequation %} וגם מדידה בבסיס {% equation %}X{% endequation %} תיתן לנו את אותו וקטור הסתברויות - סיטואציה שונה מאלו שראינו קודם, שממחישה שכשאנחנו משחזרים מצב, אנחנו לא רוצים לשחזר <strong>וקטור</strong> אלא <strong>מטריצה</strong> - את מטריצת הצפיפות שמתארת את המצב. כלומר, אם אנחנו מתעסקים עם מצב של קיוביט יחיד, אנחנו רוצים לשחזר מטריצה {% equation %}\rho=\left(\begin{array}{cc} \alpha & \beta\\ \gamma & \delta \end{array}\right){% endequation %}.

עכשיו, כשדיברנו על מטריצות צפיפות ראינו ש-{% equation %}\text{tr}\rho=1{% endequation %}, כלומר {% equation %}\alpha+\delta=1{% endequation %}, מה שאומר שאפשר להסיק את {% equation %}\delta{% endequation %} מתוך {% equation %}\alpha{% endequation %}. נשארו לנו שלושה פרמטרים שצריך להסיק - שלוש "דרגות חופש" של המטריצה. האינטואיציה שלנו מאלגברה לינארית אולי אומרת לנו שצריך, אם כן, מערכת של שלוש משוואות לינאריות שמערבת את {% equation %}\rho{% endequation %} איכשהו, וזה במקרה הממוזל שבכלל אפשר להסיק את {% equation %}\rho{% endequation %} ממערכת משוואות לינארית שכזו. זה מה שיפה כאן - בתנאים האידאליים שלנו (שבהם וקטורי ההסתברויות נתונים לנו במדויק) זה אכן כל מה שצריך, פתרון של מערכת משוואות לינארית. אבל איזו?

כזכור מהפוסט הקודם על מטריצות צפיפות, אם אני במצב {% equation %}\rho{% endequation %} ואני מודד אותו עם קבוצת אופרטורי מדידה כלשהי, אז ההסתברות ש-{% equation %}M_{i}{% endequation %} יעלה בגורל היא {% equation %}p\left(i\right)=\text{tr}\left(M_{i}^{\dagger}M_{i}\rho\right){% endequation %}. זו אחלה משוואה בזכות עצמה, אבל אם רוצים לפשט אותה קצת, אפשר לעבור שוב ללשון של וקטורים. על מטריצה {% equation %}A{% endequation %} מסדר {% equation %}n\times m{% endequation %} קל מאוד לחשוב בתור וקטור מאורך {% equation %}n\cdot m{% endequation %}: נאמר, וקטור שמכיל קודם כל את אברי <strong>השורה הראשונה</strong> של {% equation %}A{% endequation %}, ואז השורה השניה וכן הלאה; או <strong>העמודה הראשונה</strong> של {% equation %}A{% endequation %} ואז העמודה השניה וכן הלאה. אני אלך לפי הקונבנציה שלוקחים את <strong>השורות</strong> בזו אחר זו, אבל שתי הגישות נפוצות ואין עדיפות עקרונית לאחת מהן.

אם כן, אם אם {% equation %}A{% endequation %} היא מטריצה מסדר {% equation %}n\times m{% endequation %}, אני אסמן ב-{% equation %}\left|\left.A\right\rangle \right\rangle {% endequation %} את וקטור <strong>העמודה</strong> מאורך {% equation %}n\cdot m{% endequation %} שאבריו לפי הסדר הם {% equation %}a_{11},\ldots,a_{1m},a_{21},\ldots,a_{nm}{% endequation %}. הנה דוגמא קונקרטית עבור מטריצת {% equation %}2\times3{% endequation %}:

{% equation %}A=\left(\begin{array}{ccc} a_{11} & a_{12} & a_{13}\\ a_{21} & a_{22} & a_{23} \end{array}\right){% endequation %}

במקרה הזה נקבל

{% equation %}\left|\left.A\right\rangle \right\rangle =\left(\begin{array}{cccccc} a_{11} & a_{12} & a_{13} & a_{21} & a_{22} & a_{23}\end{array}\right)^{T}{% endequation %}

עכשיו, כמו שהגדרתי בשעתו {% equation %}\left\langle \psi\right|=\left(\left|\psi\right\rangle \right)^{\dagger}{% endequation %} אני יכול להגדיר גם {% equation %}\left\langle \left\langle A\right.\right|=\left(\left|\left.A\right\rangle \right\rangle \right)^{\dagger}{% endequation %}, ואז אני מקבל את השוויון היפה

{% equation %}\left\langle \left\langle A\right.\right|\left|\left.B\right\rangle \right\rangle =\text{tr}\left(A^{\dagger}B\right){% endequation %}

קל לבדוק שזה אכן מתקיים:

{% equation %}\text{tr}\left(A^{\dagger}B\right)=\sum_{k=1}^{m}\left[A^{\dagger}B\right]_{kk}=\sum_{k=1}^{m}\sum_{i=1}^{n}\left[A^{\dagger}\right]_{ki}\left[B\right]_{ik}={% endequation %}

{% equation %}=\sum_{k=1}^{m}\sum_{i=1}^{n}\overline{\left[A\right]_{ik}}\left[B\right]_{ik}=\left\langle \left\langle A\right.\right|\left|\left.B\right\rangle \right\rangle {% endequation %}

שימו לב שהמעבר האחרון לא כל כך מתעניין בשאלה אם האופן שבו {% equation %}A,B{% endequation %} הפכו לוקטור היה לפי שורות, עמודות, או כל סדר אחר; לכן הבחירה שלי ללכת על פי שורות היא קונבנציה ולא משהו קריטי.

אגב, לא נכנסתי לפרטים הללו כאן, אבל {% equation %}\text{tr}\left(A^{\dagger}B\right){% endequation %} מגדיר לנו <strong>מכפלה פנימית</strong> על המרחב הוקטורי של המטריצות מהסדר המתאים; זו לא פעולה אקראית שצצה משום מקום. בהקשר שלנו, {% equation %}\text{tr}\left(M_{i}^{\dagger}M_{i}\rho\right){% endequation %} זה הערך שמעניין אותנו, ואנחנו יכולים לנצל את זה ש-{% equation %}\left(M_{i}^{\dagger}M_{i}\right)^{\dagger}=M_{i}^{\dagger}M_{i}{% endequation %} כדי לכתוב

{% equation %}p\left(i\right)=\left\langle \left\langle M_{i}^{\dagger}M_{i}\right.\right|\left|\left.\rho\right\rangle \right\rangle {% endequation %}

למעשה, כדי לפשט עניינים, נוח לסמן {% equation %}E_{i}=M_{i}^{\dagger}M_{i}{% endequation %} ולעבור לתאר מדידות עם ה-{% equation %}E_{i}{% endequation %}-ים הללו, שמקיימים {% equation %}\sum E_{i}=I{% endequation %} וכל {% equation %}E_{i}{% endequation %} הוא מטריצה חיובית (במובן שתיארתי בפוסט הקודם: {% equation %}\left\langle \psi\right|E_{i}\left|\psi\right\rangle >0{% endequation %} לכל {% equation %}\left|\psi\right\rangle \ne0{% endequation %}). אפשר לעשות את ההפך, <strong>להתחיל</strong> מסט של אופרטורים שמקיימים את שתי התכונות הללו ולהסיק ממנו {% equation %}M_{i}{% endequation %}-ים שנותנים לנו מדידה; הפורמליזם שבו עובדים עם ה-{% equation %}E_{i}{% endequation %}-ים נקרא פורמליזם ה-POVM (ראשי תיבות של Positive Operator Valued Measurements), אבל אני לא נכנס לעובי הקורה הזה.

סיכום ביניים: אם יש לי מדידה עם אופרטור מתאים {% equation %}E_{i}{% endequation %}, אני מקבל

{% equation %}p\left(i\right)=\left\langle \left\langle E_{i}\right.\right|\left|\left.\rho\right\rangle \right\rangle {% endequation %}

את הפעולה הזו אפשר לתאר בתור כפל של השורה {% equation %}\left\langle \left\langle E_{i}\right.\right|{% endequation %} בעמודה {% equation %}\left|\left.\rho\right\rangle \right\rangle {% endequation %}, והיא מתאימה לתוצאה אפשרית <strong>אחת </strong>של מדידה אפשרית <strong>אחת</strong> של {% equation %}\rho{% endequation %}. אני יכול לאסוף בצורה הזו הרבה שורות, שמתאימות למדידות שונות, ולקבל מטריצה {% equation %}M{% endequation %}, ואז יש לי את מערכת המשוואות

{% equation %}M\left|\left.\rho\right\rangle \right\rangle =\vec{p}{% endequation %}

כאשר {% equation %}\vec{p}{% endequation %} הוא וקטור ההסתברויות: וקטור של סקלרים, שבו הכניסה ה-{% equation %}i{% endequation %} מתאימה למדידה על פי האופרטור שרשום בשורה ה-{% equation %}i{% endequation %} של {% equation %}M{% endequation %}.

כל זה מתוסבך נורא, אז בואו נראה דוגמא קונקרטית עבור המקרה של קיוביט בודד. כבר דיברתי על מדידה של קיוביט בבסיסים {% equation %}Z,X{% endequation %} שנגזרים מאופרטורי פאולי {% equation %}X,Z{% endequation %}; אני אזכיר איך בדיוק הם נגזרים, ואעשה את אותו דבר בדיוק גם עבור {% equation %}Y{% endequation %}.

נתחיל עם {% equation %}X=\left(\begin{array}{cc} 0 & 1\\ 1 & 0 \end{array}\right){% endequation %}. הרעיון הוא שבגלל שזה אופרטור הרמיטי, קיים לו <strong>פירוק ספקטרלי</strong>, כלומר שאפשר לכתוב {% equation %}X=\sum\lambda P_{\lambda}^{X}{% endequation %}: צירוף לינארי שהמקדמים {% equation %}\lambda{% endequation %} שלו הם הערכים העצמיים השונים של {% equation %}X{% endequation %} ו-{% equation %}P_{\lambda}^{X}{% endequation %} הוא אופרטור ההטלה למרחב העצמי שמתאים ל-{% equation %}\lambda{% endequation %}. עבור {% equation %}X{% endequation %} (וגם עבור {% equation %}Y,Z{% endequation %}) הערכים העצמיים הם {% equation %}\pm1{% endequation %} ולכן מקבלים

{% equation %}X=1\cdot P_{1}^{X}+\left(-1\right)\cdot P_{-1}^{X}{% endequation %}

בדיקה זריזה מעלה ש-

{% equation %}P_{1}^{X}=\frac{1}{2}\left(\begin{array}{cc} 1 & 1\\ 1 & 1 \end{array}\right),P_{-1}^{X}=\frac{1}{2}\left(\begin{array}{cc} 1 & -1\\ -1 & 1 \end{array}\right){% endequation %}

עבור {% equation %}Y=\left(\begin{array}{cc} 0 & -i\\ i & 0 \end{array}\right){% endequation %} נקבל

{% equation %}P_{1}^{Y}=\frac{1}{2}\left(\begin{array}{cc} 1 & -i\\ i & 1 \end{array}\right),P_{-1}^{Y}=\frac{1}{2}\left(\begin{array}{cc} 1 & i\\ -i & 1 \end{array}\right){% endequation %}

ועבור {% equation %}Z=\left(\begin{array}{cc} 1 & 0\\ 0 & -1 \end{array}\right){% endequation %} נקבל

{% equation %}P_{1}^{Z}=\left(\begin{array}{cc} 1 & 0\\ 0 & 0 \end{array}\right),P_{-1}^{Z}=\left(\begin{array}{cc} 0 & 0\\ 0 & 1 \end{array}\right){% endequation %}

ה-{% equation %}P{% endequation %}-ים הללו הם ה-{% equation %}M_{i}{% endequation %}-ים בשיטת הכתיב הקודמת שלי, כך שאנחנו רוצים לקבל מהם את {% equation %}E_{i}=M_{i}^{\dagger}M_{i}{% endequation %}, אבל מכיוון שאלו אופרטורים הרמיטיים (כלומר {% equation %}M_{i}^{\dagger}=M_{i}{% endequation %}) והטלות (כלומר {% equation %}M_{i}^{2}=M_{i}{% endequation %}) נקבל בדיוק את אותם אופרטורים. אז כדי לבנות את המטריצה {% equation %}M{% endequation %} שדיברתי עליה צריך לעשות שני דברים: לפרוש אותם לשורה אחת ארוכה כל אחד, ולהצמיד את האיברים (כי כזכור, {% equation %}\left\langle \left\langle E_{i}\right.\right|{% endequation %} מסמל את {% equation %}\left(\left|\left.E_{i}\right\rangle \right\rangle \right)^{\dagger}{% endequation %}). לכן {% equation %}P_{1}^{Y}{% endequation %} יהפוך אל {% equation %}\left(\begin{array}{cccc} \frac{1}{2} & -\frac{i}{2} & \frac{i}{2} & \frac{1}{2}\end{array}\right){% endequation %} אחרי השיטוח ואל {% equation %}\left(\begin{array}{cccc} \frac{1}{2} & \frac{i}{2} & -\frac{i}{2} & \frac{1}{2}\end{array}\right){% endequation %} אחרי ההצמדה. בסך הכל נקבל את המטריצה

{% equation %}M=\left(\begin{array}{cccc} \frac{1}{2} & \frac{1}{2} & \frac{1}{2} & \frac{1}{2}\\ \frac{1}{2} & -\frac{1}{2} & -\frac{1}{2} & \frac{1}{2}\\ \frac{1}{2} & \frac{i}{2} & -\frac{i}{2} & \frac{1}{2}\\ \frac{1}{2} & -\frac{i}{2} & \frac{i}{2} & \frac{1}{2}\\ 1 & 0 & 0 & 0\\ 0 & 0 & 0 & 1 \end{array}\right){% endequation %}

עכשיו, הרעיון הוא כזה: יש לנו מצב קוונטי {% equation %}\rho{% endequation %} שאנחנו לא יודעים מהו. אנחנו מודדים אותו בבסיסים {% equation %}X,Y,Z{% endequation %} ומקבלים התפלגות של תוצאות. לכל בסיס אנחנו מקבלים שתי תוצאות, אחת לכל אחד מהערכים העצמיים (שתי התוצאות הללו מסתכמות ל-1, אז הן לא בלתי תלויות זו בזו). את התוצאות הללו אנחנו מכניסים לוקטור {% equation %}\vec{p}{% endequation %}, ואז אנחנו מקבלים<strong> מערכת משוואות לינארית:</strong>

{% equation %}M\left|\left.\rho\right\rangle \right\rangle =\vec{p}{% endequation %}

כאן {% equation %}M,\vec{p}{% endequation %} ידועים ו-{% equation %}\left|\left.\rho\right\rangle \right\rangle {% endequation %} הוא הנעלם שאנחנו רוצים לשחזר. איך פותרים מערכת משוואות לינארית? בדרך כלל מחשבים את {% equation %}M^{-1}{% endequation %} וכופלים בה את שני האגפים ומקבלים {% equation %}\left|\left.\rho\right\rangle \right\rangle =M^{-1}\vec{p}{% endequation %}, אלא שזה פשוט לא יכול לעבוד כאן, כי {% equation %}M{% endequation %} <strong>גדולה מדי</strong> - היא לא מטריצה ריבועית. יש לה רק ארבע עמודות, אבל שש שורות. אפשר, כמובן, להסיר חלק מהשורות הללו, אבל אפשר גם לעשות משהו אחר.

כאמור, {% equation %}M{% endequation %} היא לא מטריצה ריבועית, אבל {% equation %}M^{\dagger}M{% endequation %} היא כן מטריצה ריבועית, ובתקווה היא גם הפיכה (במקרה שלנו היא אכן יוצאת הפיכה; אם היא לא יוצאת הפיכה זה אומר שבחרנו למדוד את {% equation %}\rho{% endequation %} בשילוב בסיסים שהוא לא <strong>מלא טומוגרפית</strong> - אי אפשר להשתמש בו בשביל טומוגרפיה). ועכשיו תראו איזה קסם אני עושה. אני מתחיל עם {% equation %}M\left|\left.\rho\right\rangle \right\rangle =\vec{p}{% endequation %}, כופל את שני האגפים ב-{% equation %}M^{\dagger}{% endequation %} ומקבל {% equation %}M^{\dagger}M\left|\left.\rho\right\rangle \right\rangle =M^{\dagger}\vec{p}{% endequation %}, ואז אני כופל בהופכית של {% equation %}M^{\dagger}M{% endequation %} ומקבל:

{% equation %}\left|\left.\rho\right\rangle \right\rangle =\left(M^{\dagger}M\right)^{-1}M^{\dagger}\vec{p}{% endequation %}

וכך אני מצליח לשחזר את {% equation %}\rho{% endequation %} המקורית!

בואו נראה איך זה עובד בפועל. אם תחשבו, תקבלו ש-

{% equation %}M^{\dagger}M=\left(\begin{array}{cccc} 2 & 0 & 0 & 1\\ 0 & 1 & 0 & 0\\ 0 & 0 & 1 & 0\\ 1 & 0 & 0 & 2 \end{array}\right){% endequation %}

ההופכית שלה היא

{% equation %}\left(M^{\dagger}M\right)^{-1}=\left(\begin{array}{cccc} \frac{2}{3} & 0 & 0 & -\frac{1}{3}\\ 0 & 1 & 0 & 0\\ 0 & 0 & 1 & 0\\ -\frac{1}{3} & 0 & 0 & \frac{2}{3} \end{array}\right){% endequation %}

ולכן מקבלים בסוף

{% equation %}\left(M^{\dagger}M\right)^{-1}M^{\dagger}=\left(\begin{array}{cccccc} \frac{1}{6} & \frac{1}{6} & \frac{1}{6} & \frac{1}{6} & \frac{2}{3} & -\frac{1}{3}\\ \frac{1}{2} & -\frac{1}{2} & -\frac{i}{2} & \frac{i}{2} & 0 & 0\\ \frac{1}{2} & -\frac{1}{2} & \frac{i}{2} & -\frac{i}{2} & 0 & 0\\ \frac{1}{6} & \frac{1}{6} & \frac{1}{6} & \frac{1}{6} & -\frac{1}{3} & \frac{2}{3} \end{array}\right){% endequation %}

זו המטריצה הקסומה שכשכופלים אותה בוקטור ההסתברויות {% equation %}\vec{p}{% endequation %} שקיבלנו מהניסוי, משחזרים את המצב {% equation %}\rho{% endequation %} המקורי. בואו ננסה למשל לשחזר את {% equation %}\rho{% endequation %} שמתאר את הסיטואציה שבה אנחנו ב-{% equation %}\left|0\right\rangle ,\left|1\right\rangle {% endequation %} בהסתברות חצי-חצי. אנחנו כבר יודעים שתוצאות המדידה בבסיס {% equation %}X{% endequation %} הולכות להיות {% equation %}\left(\frac{1}{2},\frac{1}{2}\right){% endequation %} בגלל שלא משנה אם אנחנו ב-{% equation %}\left|0\right\rangle {% endequation %} או ב-{% equation %}\left|1\right\rangle {% endequation %}, מדידה בבסיס {% equation %}X{% endequation %} מתפלגת חצי-חצי עבור שני המצבים הללו. בנוסף אנחנו יודעים שגם המדידה בבסיס {% equation %}Z{% endequation %} הולכת להיות {% equation %}\left(\frac{1}{2},\frac{1}{2}\right){% endequation %} מסיבה שונה: אם אנחנו ב-{% equation %}\left|0\right\rangle {% endequation %} אז המדידה תחזיר בודאות {% equation %}\left|0\right\rangle {% endequation %} אבל אנחנו ב-{% equation %}\left|0\right\rangle {% endequation %} רק בהסתברות {% equation %}\frac{1}{2}{% endequation %} מראש. מה שעוד לא דיברתי עליו הוא מה קורה במדידה בבסיס {% equation %}Y{% endequation %}, אבל חישוב עם הנוסחה {% equation %}p\left(i\right)=\left\langle \psi\right|E_{i}\left|\psi\right\rangle {% endequation %} מראה שגם במקרה זה, לא משנה אם אנחנו ב-{% equation %}\left|0\right\rangle {% endequation %} או ב-{% equation %}\left|1\right\rangle {% endequation %}, ההסתברות לכל תוצאה היא {% equation %}\frac{1}{2}{% endequation %}. לכן בסך הכל 

{% equation %}\vec{p}=\left(\begin{array}{c} \frac{1}{2}\\ \frac{1}{2}\\ \frac{1}{2}\\ \frac{1}{2}\\ \frac{1}{2}\\ \frac{1}{2} \end{array}\right){% endequation %}

עכשיו נחשב ונקבל

{% equation %}\left(M^{\dagger}M\right)^{-1}M^{\dagger}\vec{p}=\left(\begin{array}{c} \frac{1}{2}\\ 0\\ 0\\ \frac{1}{2} \end{array}\right){% endequation %}

וכשמשחזרים מזה את המטריצה המקורית מקבלים {% equation %}\left(\begin{array}{cc} \frac{1}{2} & 0\\ 0 & \frac{1}{2} \end{array}\right){% endequation %}, כפי שציפינו.

מה אם במקום זה היינו במצב {% equation %}\left|+\right\rangle {% endequation %} בהתחלה? כזכור, זה משפיע על המדידות בבסיס {% equation %}X{% endequation %} שיוצאות {% equation %}\left(\begin{array}{c} 1\\ 0 \end{array}\right){% endequation %}, אבל אם עושים את החישובים עבור בסיסים {% equation %}Y,Z{% endequation %} עדיין מקבלים חצי חצי, כלומר וקטור ההסתברויות במקרה זה הוא

{% equation %}\left(\begin{array}{c} 1\\ 0\\ \frac{1}{2}\\ \frac{1}{2}\\ \frac{1}{2}\\ \frac{1}{2} \end{array}\right){% endequation %}

ועכשיו מקבלים:

{% equation %}\left(M^{\dagger}M\right)^{-1}M^{\dagger}\vec{p}=\left(\begin{array}{c} \frac{1}{2}\\ \frac{1}{2}\\ \frac{1}{2}\\ \frac{1}{2} \end{array}\right){% endequation %}

כלומר {% equation %}\rho=\left(\begin{array}{cc} \frac{1}{2} & \frac{1}{2}\\ \frac{1}{2} & \frac{1}{2} \end{array}\right){% endequation %} כמו שציפינו לקבל.

יפה, אז אנחנו רואים שאפשר לבצע את הקסם של שיחזור {% equation %}\rho{% endequation %} מתוך מדידות, אבל <strong>איך</strong> מבצעים את המדידות הללו? כמובן, אם אנחנו אלו שמתעסקים במחשב הקוונטי ברמת המימוש (או בניסוי הקוונטי שעושים; טומוגרפיה קוונטית לא חייבת להיות של מצב במחשב קוונטי) אנחנו אולי יכולים לממש סוגים שונים של מדידות. אבל נאמר שאנחנו עובדים עם מחשב קוונטי שיודע למדוד רק בבסיס {% equation %}Z{% endequation %}, האם יש דרך לבצע מדידות גם בבסיסים אחרים?

ובכן, יש. בואו ניזכר במשהו שכבר הראיתי פעם-פעמיים, עבור המטריצה {% equation %}H=\frac{1}{\sqrt{2}}\left(\begin{array}{cc} 1 & 1\\ 1 & -1 \end{array}\right){% endequation %}:

{% equation %}H^{\dagger}ZH=X{% endequation %}

אפשר לראות את זה על ידי חישוב מפורש. זה כמובן עובר לרמת ההטלות:

{% equation %}X=H^{\dagger}ZH=H^{\dagger}\left(P_{1}^{Z}-P_{-1}^{Z}\right)H=H^{\dagger}P_{1}^{Z}H-H^{\dagger}P_{-1}^{Z}H{% endequation %}

ומכאן אפשר להסיק שלכל מצב {% equation %}\left|\psi\right\rangle {% endequation %} מתקיים

{% equation %}\left\langle \psi\right|P_{\lambda}^{X}\left|\psi\right\rangle =\left\langle \psi\right|H^{\dagger}P_{1}^{Z}H\left|\psi\right\rangle =\left\langle H\psi\right|P_{1}^{Z}\left|H\psi\right\rangle {% endequation %}

כלומר, אפשר להמיר מדידה בבסיס {% equation %}X{% endequation %} של {% equation %}\left|\psi\right\rangle {% endequation %} במדידה בבסיס {% equation %}Z{% endequation %} של {% equation %}H\left|\psi\right\rangle {% endequation %} - התפלגות התוצאות שנקבל תהיה זהה. זה באמת מה שעושים במחשב קוונטי - מעגל אחד שפשוט מייצר את המצב הקוונטי עבור מדידה בבסיס {% equation %}Z{% endequation %}, מעגל אחר שמייצר את המצב הקוונטי ואז מפעיל עליו {% equation %}H{% endequation %} עבור מדידה בבסיס {% equation %}X{% endequation %}. ומה עם בסיס {% equation %}Y{% endequation %}? ובכן, {% equation %}SXS^{\dagger}=Y{% endequation %} עבור {% equation %}S=\left(\begin{array}{cc} 1 & 0\\ 0 & i \end{array}\right){% endequation %}, ולכן {% equation %}\left(HS^{\dagger}\right)^{\dagger}Z\left(HS^{\dagger}\right)=Y{% endequation %}, ומכאן שכדי למדוד בבסיס {% equation %}Y{% endequation %} קודם מפעילים על המצב {% equation %}S^{\dagger}{% endequation %}, אחר כך מפעילים עליו {% equation %}H{% endequation %} ואז מודדים בבסיס {% equation %}Z{% endequation %} כרגיל.

כל הדיון עד כה התעסק בסיטואציה של קיוביט בודד. אבל מה אם {% equation %}\rho{% endequation %} הוא מצב של מערכת על {% equation %}n{% endequation %} קיוביטים? נתחיל מ-{% equation %}n=2{% endequation %}. במקרה הזה, אנחנו מסתכלים על כל הזוגות {% equation %}\left(P_{1},P_{2}\right){% endequation %} כאשר {% equation %}P_{i}\in\left\{ X,Y,Z\right\} {% endequation %} - בסך הכל תשעה זוגות כאלו. כל זוג מגדיר לנו מעגל אחר עם מדידות אחרות. למשל, {% equation %}\left(X,Y\right){% endequation %} פירושו "למדוד את הקיוביט הראשון בבסיס {% equation %}X{% endequation %} ואת השני בבסיס {% equation %}Y{% endequation %}", כששתי המדידות הללו מבוצעות בצורה שתיארתי זה עתה. מה שמתקבל הוא 4 תוצאות מדידה אפשריות: {% equation %}00,01,10,11{% endequation %}, שכל אחת נותנת לנו הסתברות אחרת ותקבל שורה משלה בוקטור {% equation %}\vec{p}{% endequation %} - כלומר, זה יהיה וקטור עם 36 כניסות. עבור {% equation %}n{% endequation %} כללי, אנחנו מסתכלים על כל ה-{% equation %}n{% endequation %}-יות {% equation %}\left(P_{1},\ldots,P_{n}\right){% endequation %} כאשר {% equation %}P_{i}\in\left\{ X,Y,Z\right\} {% endequation %}. יש בסך הכל {% equation %}3^{n}{% endequation %} {% equation %}n{% endequation %}-יות כאלו וכל {% equation %}n{% endequation %}-יה כזו מגדירה {% equation %}2^{n}{% endequation %} תוצאות מדידה אפשריות... כפי שאפשר לראות, זה גדל אקספוננציאלית. זה אומר שבפועל, טומוגרפיה הופכת למשהו <strong>בלתי יישים בעליל</strong> עבור יותר ממספר זעיר של קיוביטים; מה שעושים בפועל הוא טומוגרפיה רק לחלק מהקיוביטים במערכת במקום לכולם.

הנה למשל מעגל טומוגרפיה על שני קיוביטים שקודם כל מייצר את המצב השזור {% equation %}\frac{\left|00\right\rangle +\left|11\right\rangle }{\sqrt{2}}{% endequation %} (או, אם לחדד את הפואנטה מאחורי טומוגרפיה קוונטית, קודם <strong>מנסה </strong>ליצור<strong> </strong>את המצב הזה, ומטרת הטומוגרפיה היא לראות כמה הוא הצליח בזה) ולאחר מכן מודד את הקיוביט הראשון בבסיס {% equation %}X{% endequation %} ואת השני בבסיס {% equation %}Y{% endequation %}:

<img src="{{site.baseurl}}{{site.post_images}}/2022/qst.png" alt=""/>

לסיום, אי אפשר לוותר על רגע ה"כל מה שאמרתי לכם עד כה היה שקר גמור" הבלתי נמנע. כלומר, לא שיקרתי בשום צורה, אבל כן הזנחתי את העניין המרכזי. אי שם בתחילת הפוסט אמרתי שבואו נניח לצורך פשטות שיש לי את הערכים המדויקים של {% equation %}\vec{p}{% endequation %}, שזה נחמד אבל זה <strong>לא משהו שהולך להתקבל בניסוי</strong>. בניסוי אני לא אקבל {% equation %}\frac{1}{2}{% endequation %} אלא זוועה כמו {% equation %}\frac{483}{1000}{% endequation %}. בסיטואציה כזו, הוקטור {% equation %}\vec{p}{% endequation %} שקיבלתי הוא לא מדויק; שיטת היפוך המטריצה שהצגתי לא רק שלא תחזיר את {% equation %}\rho{% endequation %} הנכונה אלא רק קירוב שלה (את זה אפשר לסבול, בכל מקרה אנחנו לא מצפים לדיוק מוחלט), אבל גרוע מזה - סביר להניח שהיא תחזיר {% equation %}\rho{% endequation %} <strong>שאינה מטריצת צפיפות</strong>, כלומר אינה בעלת עקבה 1 או שאינה חיובית. זו כבר בעיה משמעותית יותר - בדרך כלל אנחנו רוצים שטומוגרפיה תחזיר לנו מצב קוונטי שהוא קירוב של המצב האמיתי, לא שתחזיר לנו קירוב שאיננו אמיתי.

זה אומר שנוקטים בשיטת פתרון אחרת, שנעזרת בכלים סטנדרטיים של אופטימיזציה: מה שאנחנו רוצים הוא להביא למינימום את הביטוי

{% equation %}\|M\left|\left.\rho\right\rangle \right\rangle -\vec{p}\|{% endequation %}

כאשר אברי {% equation %}\left|\left.\rho\right\rangle \right\rangle {% endequation %} הם המשתנים של בעיית האופטימיזציה, והם כפופים לאילוצים נוספים שמבטיחים ש-{% equation %}\rho{% endequation %} תהיה מטריצת צפיפות תקינה. חשבתי להיכנס כאן לעובי הקורה של איך עושים את זה, ואולי אעשה את זה בהמשך, אבל נראה לי שעדיף לשמור על הפוסט הזה ממוקד יחסית.

עוד בעיה שצריך להביא בחשבון היא שחישוב קוונטי הוא תהליך <strong>רועש</strong>. זה אומר שבביצוע תהליך המדידה עצמה עשויות להצטבר בעיות; וגרוע לא פחות - גם בשערי ה-{% equation %}H{% endequation %} וה-{% equation %}S^{\dagger}{% endequation %} שאנחנו משתמשים בהם כדי למדוד בבסיסים שונים גם כן עשויות להצטבר בעיות. מה שהיינו רוצים הוא שיטת טומוגרפיה שאיכשהו מביאה את זה בחשבון, ואמנם יש כזו (במחיר של סיבוכיות הרבה יותר גדולה של מה שהיא עושה) שנקראת Gate Set Tomography, אבל לפני שאדבר עליה צריך לחזור אל השאלה שבה סיימתי את הפוסט הקודם - איך בעצם ממדלים שינויים שיכולים להתבצע על מערכת קוונטית, וספציפית איך ממדלים רעשים? 
