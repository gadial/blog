---
title: "איך מחשבים דטרמיננטה עם אלגוריתם בריס?"
layout: post
categories:
  - אלגברה לינארית
tags:
  - דטרמיננטה
---


<h2>חלק ראשון, שבו אנחנו לומדים שמינוס 32 הוא כמעט 256</h2>

<a href="https://gadial.net/2024/12/03/computing_determinants/">בפוסט הקודם שלי</a> על דטרמיננטות הסברתי איך מחשבים אותן. הצגתי שתי דרכים: אחת שהולכת דרך ההגדרה הרקורסיבית והיא מאוד לא יעילה לחישוב, ואחת שמבצעת פישוט למטריצה שרוצים לחשב את הדטרמיננטה שלה והיא משמעותית יותר יעילה. יש שיטות שהן אפילו יעילות יותר, אבל בפוסט הזה אני רוצה לקחת צעד אחד אחורה דווקא ולהציג שיטה יעילה פחות, אבל עם יתרון נחמד אחד: אם האיברים של המטריצה הם כולם מספרים שלמים, אנחנו לא נזדקק לשברים במהלך כל החישוב. למה זה טוב? תכף אתן דוגמא פשוטה.

ראשית, בואו נבין מה באלגוריתם ה"יעיל" מכריח את השברים להיכנס למשחק. בואו נסתכל במטריצה הבאה:

{% equation %}\left[\begin{array}{ccc} 2 & 1 & 3\\ 3 & 1 & 6\\ 4 & 1 & 8 \end{array}\right]{% endequation %}

האלגוריתם מבוסס על כך שאנחנו עוברים עמודה-עמודה, ובכל פעם אנחנו משתמשים באיבר כלשהו מהעמודה כדי לאפס את כל האיברים שאחריו בעמודה - זה הופך את חישוב הדטרמיננטה לפשוט כי כאשר מפתחים את הדטרמיננטה לפי עמודות, יוצא שבכל פעם יש רק איבר אחד בכל עמודה שצריך לפתח לפיו, ולכן מה שהוא בדרך כלל חישוב רקורסיבי מסובך שמתפצל להרבה מקרים לא מתפצל בכלל. כדי לאפס איברים בעמודה משתמשים בתוצאה המרהיבה לפיה אם לוקחים שורה במטריצה, ומחברים אותה עם שורה אחרת כשהיא מוכפלת בסקלר כלשהו, התוצאה היא בעלת אותה דטרמיננטה כמו המטריצה המקורית. למשל, אם במטריצה לעיל אני אקח את השורה הראשונה, אכפול אותה ב-{% equation %}-2{% endequation %} ואחבר לשורה האחרונה, אני אקבל את המטריצה

{% equation %}\left[\begin{array}{ccc} 2 & 1 & 3\\ 3 & 1 & 6\\ 0 & -1 & 2 \end{array}\right]{% endequation %}

והמטריצה הזו היא בעלת אותה דטרמיננטה בדיוק כמו המטריצה שהתחלתי ממנה, והנה - קיבלתי אפס בעמודה הראשונה. הבעיה היא שכדי להיפטר מה-3 שבשורה האמצעית אני צריך לכפול את השורה הראשונה במשהו שאינו מספר שלם - ב-{% equation %}-\frac{3}{2}{% endequation %}, מה שמוביל אותי למטריצה הבאה:

{% equation %}\left[\begin{array}{ccc} 2 & 1 & 3\\ 0 & -\frac{1}{2} & \frac{3}{2}\\ 0 & -1 & 2 \end{array}\right]{% endequation %}

וזהו, עכשיו יש לי שברים בתוך המטריצה, למרות שהתחלתי עם מטריצה שכולה מספרים שלמים ולמרות <strong>שגם התוצאה תהיה מספר שלם</strong>. כדי לראות שהתוצאה תהיה מספר שלם מספיק להיזכר באופן שבו דטרמיננטה מוגדרת רקורסיבית: אנחנו מקבלים סכום של איברים שכל אחד מהם שייך למטריצה (כלומר הוא מספר שלם) שמוכפל ב-{% equation %}\pm1{% endequation %} (מספר שלם) וזה מוכפל בדטרמיננטה של תת-מטריצות שמתקבלות מהמטריצה המקורית על ידי מחיקת שורות ועמודות (ולכן גם בהן יש מספרים שלמים). לי הסיטואציה הזו טיפה מזכירה את המקרה של ה-Casus irreducibilis בפתרון משוואות ממעלה שלישית (<a href="https://gadial.net/2018/07/26/casus_irreducibilis/">יש לי פוסט על זה</a>): שם העניין הוא שיש לנו משוואה פולינומית עם מקדמים שהם מספרים ממשיים, והפתרונות שלה כולם מספרים ממשיים, אבל בלי לעבור "דרך" המספרים המרוכבים (כלומר, להוציא שורש ריבועי למספר שלילי) לא נוכל לכתוב את הפתרונות הללו באמצעות נוסחה. אלא שיש הבדל מהותי - במקרה ההוא <strong>חייבים</strong> לעבור דרך המרוכבים (יש לזה הוכחה די מרהיבה באמצעות תורת גלואה שאני מראה בפוסט ההוא) אבל במקרה שלנו זה לא הכרחי. יש דרכים אחרות לחשב את הדטרמיננטה גם בלי להכניס שברים למשחק. כבר ראינו אחת: לחשב את הדטרמיננטה באמצעות האלגוריתם הרקורסיבי, אלא שזה כאמור פשוט לא יעיל ולכן בפוסט הזה אני אציג את מה שנקרא "האלגוריתם של ברייס" (Bareiss) ששומר על הכל שלם והנזק שהוא גורם לזמן הריצה הוא לא כזה משמעותי (אבל יש נזק; זה בהחלט אלגוריתם שבעייתי בשלל סיטואציות ולכן טוב שמכירים אותו <strong>וגם</strong> שיטות אחרות).

בואו נדבר שניה על המוטיבציה האישית שלי לכתוב את הפוסט כדי להבין למה לא כדאי לסמוך בעיניים עצומות על השיטות הקיימות ולמה לפעמים חשוב לדבוק במספרים שלמים במקום בשברים. נסיבות אלו ואחרות הובילו אותי לחשב דטרמיננטה של מטריצה {% equation %}5\times5{% endequation %}, שנותנת לנו את הנפח של טטרהדרון (פירמידה עם בסיס משולש) שאורכי הצלעות שלו נתונים על ידי {% equation %}d_{ij}{% endequation %} עבור {% equation %}1\le i,j\le4{% endequation %}. הנפח {% equation %}V{% endequation %} נתון באמצעות

{% equation %}288V^{2}=\left|\begin{array}{ccccc} 0 & 1 & 1 & 1 & 1\\ 1 & 0 & d_{12}^{2} & d_{13}^{2} & d_{14}^{2}\\ 1 & d_{21}^{2} & 0 & d_{23}^{2} & d_{24}^{2}\\ 1 & d_{31}^{2} & d_{32}^{2} & 0 & d_{34}^{2}\\ 1 & d_{41}^{2} & d_{42}^{2} & d_{43}^{2} & 0 \end{array}\right|{% endequation %}

הדטרמיננטה הזו נקראת <strong>דטרמיננטת קיילי-מנגר</strong> והיא ראויה לפוסט בפני עצמה (היא עושה יותר מאשר לחשב נפח של טטרהדרון) והאמת העצובה היא שהדרך הכי פשוטה לחשב אותה היא פשוט להשתמש בנוסחה הרקורסיבית - זו בסך הכל מטריצת {% equation %}5\times5{% endequation %}, הרקורסיה תסתיים כמעט מייד, ואין צורך באלגוריתם שאני הולך להציג - אבל את זה נזכרתי לנסות רק אחרי שכבר מימשתי את האלגוריתם (כי על מי אני עובד, כל כך התלהבתי מהאלגוריתם שהייתי חייב לממש אותו בכל מקרה). אבל למה היא גרמה לי להגיע אל אלגוריתם בריס מלכתחילה? ובכן, כי עשיתי את הטעות של לחשב אותה באמצעות numpy. מבלי להיכנס לפרטים, המטרה שלי הייתה למצוא אורכי צלעות שעבורם הדטרמיננטה תהיה שווה בדיוק ל-256. עכשיו, בואו נניח שיש לנו מספר שלם {% equation %}n{% endequation %} כלשהו ואנחנו מסתכלים על הדטרמיננטה

{% equation %}\left|\begin{array}{ccccc} 0 & 1 & 1 & 1 & 1\\ 1 & 0 & 1 & n^{2} & n^{2}\\ 1 & 1 & 0 & \left(n-1\right)^{2} & \left(n-1\right)^{2}\\ 1 & n^{2} & \left(n-1\right)^{2} & 0 & 4\\ 1 & n^{2} & \left(n-1\right)^{2} & 4 & 0 \end{array}\right|{% endequation %}

שהיא מקרה פרטי של הדטרמיננטה לעיל עבור סדרת האורכים {% equation %}1,n,n,n-1,n-1,2{% endequation %}. אם מחשבים את הדטרמיננטה בצורה סימבולית (כלומר, פשוט פותחים את הביטוי, מקבלים פולינום ב-{% equation %}n{% endequation %} ומפשטים אותו) מקבלים {% equation %}-32{% endequation %}, כלומר הערך של הדטרמיננטה הזו לא תלוי ב-{% equation %}n{% endequation %}. למי שתוהים איך עושים את זה במחשב בלי לעבור את התהליך המהנה של לחשב ידנית דטרמיננטה {% equation %}5\times5{% endequation %}, אפשר לעשות את זה עם ספריית הפייתון sympy:

{% highlight python %}
import sympy as sp

n = sp.symbols('n')
matrix = sp.Matrix([
    [0, 1, 1, 1, 1],
    [1, 0, 1, n**2, n**2],
    [1, 1, 0, (n-1)**2, (n-1)**2],
    [1, n**2, (n-1)**2, 0, 4],
    [1, n**2, (n-1)**2, 4, 0]
])
determinant = matrix.det()
print(sp.simplify(determinant))
{% endhighlight %}

טוב ויפה, אלא שאני לא השתמשתי ב-sympy כי בדקתי שלל דטרמיננטות משלל סוגים ולא רק מהמבנה הספציפי הזה שאותו מצאתי אחר כך. ספציפית, אני בדקתי את הדטרמיננטה שמתקבלת עבור הערך {% equation %}n=524,283{% endequation %} וחישבתי אותו בעזרת הספריה הסטנדרטית לחישובים נומריים בפייתון - numpy. ומה ש-numpy נתנה הוא את התוצאה {% equation %}255.99999991524982{% endequation %}.

במבט ראשון, התוצאה הזו היא "זה 256, פשוט numpy משתמשת בייצוג שברים עם נקודה צפה ולכן יש אי דיוקים קטנים". אבל לא! זו דרך טובה לעבוד על עצמנו! כי אם אני מכניס {% equation %}n=524,283{% endequation %} ואז עוד מעלה דברים בריבוע, אני עובד עם מספרי ענק ולכן יש לי שגיאות דיוק גדולות, וחישובים שקשורים במטריצות יכולים להיות מאוד רגישים לשגיאות דיוק, וזה מתנפח ומתנפח. התוצאה, כאמור, הייתה אמורה להיות {% equation %}-32{% endequation %}; זה שהגענו אל כמעט 256 זה סתם מקרה (על ידי ערכים שונים של {% equation %}n{% endequation %} אפשר להגיע קרוב לשלל מספרים שלמים לא קשורים, פשוט 256 היה מה שחיפשנו). הנה קוד פייתון שמשתמש ב-numpy ומאפשר לראות מה הולך פה. עבור {% equation %}n=1{% endequation %} החישוב מדויק כמעט לחלוטין, וכך גם עבור {% equation %}n=10,000{% endequation %}; אבל כשהוא נשבר, הוא נשבר <strong>חזק</strong>.

{% highlight python %}
import numpy as np
for n in [1, 10000, 524283]:
    A = np.array([[0, 1,    1,        1,        1],
                  [1, 0,    1,        n**2,     n**2],
                  [1, 1,    0,        (n-1)**2, (n-1)**2],
                  [1, n**2, (n-1)**2, 0,         4],
                  [1, n**2, (n-1)**2, 4,         0]]
                  )
    print(np.linalg.det(A))
{% endhighlight %}

הבעיה פה היא כאמור ש-numpy מייצג שברים בשיטת הנקודה הצפה, ולכן יש לו רמת דיוק מוגבלת, בעוד שבפייתון יש רמת דיוק בלתי מוגבלת לעבודה עם מספרים שלמים. אז מכיוון שחשדתי ש-numpy מרמה אותי החלטתי שאני לא צריך להתעצל ולהסתמך עליו או אפילו לחפש ספריה אחרת שמבצעת את החישוב (כי אולי גם היא תרמה אותי?) אלא פשוט לממש את זה בעצמי. עכשיו, <strong>הייתי יכול</strong> להשתמש באלגוריתם הרקורסיבי הנאיבי; וגם <strong>הייתי יכול</strong> להשתמש בשיטה מבוססת השברים שראינו, ופשוט להשתמש בספריה frac בפייתון שמאפשרת ייצוג של שברים עם דיוק לא מוגבל. אבל באותו הרגע הדבר הראשון שעלה לי לראש היה לחפש "אלגוריתם לחישוב דטרמיננטה שלא משתמש בשברים" ואני שמח שזה קרה כי אלגוריתם בריס הוא די מגניב גם אם הייתי יכול להסתדר בלעדיו.

אז בואו נדבר עליו סוף סוף.

<h2>חלק שני שבו אנו רואים את מה שלשמו התכנסנו פה</h2>

קודם כל, מה אלגוריתם בריס <strong>לא</strong> עושה: הוא לא מעביר את המטריצה {% equation %}A{% endequation %} שלנו למטריצה אחרת {% equation %}B{% endequation %} כך ש-{% equation %}\left|A\right|=\left|B\right|{% endequation %}, כמו האלגוריתם היעיל שהצגתי. זה לא הולך לקרות. אני כן הולך להפוך את {% equation %}A{% endequation %} למטריצה אחרת {% equation %}B{% endequation %}, אבל יהיו להן דטרמיננטות שונות לגמרי והרעיון הוא שבסיום האלגוריתם, {% equation %}\left[B\right]_{nn}{% endequation %} (הכניסה הימנית-תחתונה של {% equation %}B{% endequation %}) תהיה שווה ל-{% equation %}\left|A\right|{% endequation %}. יותר מכך - אין בעצם סיבה להציג את האלגוריתם בתור אוסף של שינויים של המטריצה {% equation %}A{% endequation %} (ובמאמר שלו עליו אני מתבסס כאן, Sylvester's Identity and Multistep Integer Preserving Gaussian Elimination, בריס באמת לא מציג אותו ככה). אפשר לחשוב על האלגוריתם גם ככה: אם בהתחלה האיבר הכללי של {% equation %}A{% endequation %} הוא {% equation %}a_{ij}{% endequation %} (עבור {% equation %}1\le i,j\le n{% endequation %}) אז האלגוריתם מייצר סדרה של איברים {% equation %}a_{ij}^{\left(0\right)},a_{ij}^{\left(1\right)},\ldots a_{ij}^{\left(n-1\right)}{% endequation %} כך שבסופו של דבר יוצא ש-{% equation %}a_{nn}^{\left(n-1\right)}=\left|A\right|{% endequation %}. ה"חזקה" של האיברים היא לא חזקה אלא אינדקס של השלב באלגוריתם שבו אנחנו נמצאים כרגע, והאתחול הוא {% equation %}a_{ij}^{\left(0\right)}=a_{ij}{% endequation %}. בפועל, כשמממשים את האלגוריתם, הכי נוח באמת לבצע שינויים מקומיים ב-{% equation %}A{% endequation %} כדי לשמור את המספרים של השלב הבא - זה חוסך זיכרון.

אז איך עובד האלגוריתם? אין שום טעם להציג אותו כרגע כי לא נבין כלום ממה שהולך שם. זה לא הולך למנוע ממני להציג אותו בכל מקרה כי זה לפחות יוצר עניין - אני קודם כל מימשתי את האלגוריתם ורק אז תהיתי למה בעצם זה עובד. הרעיון, כאמור, הוא לעבוד בשלבים, כשבשלב מספר {% equation %}k{% endequation %} אנחנו מעדכנים את המספרים {% equation %}a_{ij}^{\left(k\right)}{% endequation %} שעדיין רלוונטיים לנו (כמו בחישוב דטרמיננטה רגיל, ככל שמתקדמים בשלבים כך פחות ופחות איברים הופכים לרלוונטיים לנו. 

הנה האלגוריתם:

<ul> <li>אתחל את המשתנים {% equation %}a_{ij}^{\left(0\right)}=a_{ij}{% endequation %} לכל {% equation %}1\le i,j\le n{% endequation %} ואת המשתנה המיוחד {% equation %}a_{00}^{\left(-1\right)}=1{% endequation %}.</li>


<li>לכל {% equation %}k=1,2,\ldots,n-1{% endequation %}: </li>
<ul>
<li>לכל {% equation %}k+1\le i,j\le n{% endequation %}, קבעו {% equation %}a_{ij}^{\left(k\right)}\leftarrow\frac{a_{ij}^{\left(k-1\right)}a_{kk}^{\left(k-1\right)}-a_{ik}^{\left(k-1\right)}a_{kj}^{\left(k-1\right)}}{a_{k-1,k-1}^{\left(k-2\right)}}{% endequation %}</li>

</ul>

</ul>

<li>החזירו את {% equation %}a_{nn}^{\left(n-1\right)}{% endequation %}</li>

בקיצור, האלגוריתם די דומה למה שקורה באלגוריתם הרגיל - גם פה פשוט מעדכנים באופן סדרתי כניסות עם כל מני מכפלות וחיסורים ו... רגע... האם זה רק אני או שיש סימן <strong>חילוק</strong> ענקי באמצע האלגוריתם? איך בדיוק פתרנו את הבעיה? ובכן, הרעיון הוא שבסימן החילוק שמופיע שם, המכנה מחלק את המונה <strong>בלי שארית</strong>. במילים אחרות - אנחנו צריכים לבצע פעולת חילוק, אבל פעולת <strong>חילוק שלמים</strong> שיכולה להיות מדויקת, ובשום שלב אנחנו לא צריכים לעבוד עם מספר שהוא שבר (אם תקראו את הפוסט עד כה תראו שנמנעתי בזהירות מלטעון דברים מופרכים כמו "האלגוריתם לא מבצע חילוק").

אוקיי, אבל למה זה עובד? במאמר שלו שעליו אני מתבסס כאן, בריס מביא טיעון לא טריוויאלי, שאולי היה אפשר להחליף בטיעונים אלמנטריים יותר (יש לבריס מאמר מוקדם יותר שבו יש טיעונים כאלו) אבל אני דווקא מאוד אוהב את הטכניקה שלו, אז בואו נראה אותה במלואה.

<h2>חלק שלישי שבו קורים קסמים עם מטריצות בלוקים</h2>

באלגוריתם שהצגתי, {% equation %}a_{ij}^{\left(k\right)}{% endequation %} חושב באמצעות תרגיל מפוקפק כלשהו (שבמסגרתו הבטחתי שתתבצע חלוקה ללא שארית). זה לא ממש עוזר לנו להבין מה הולך פה, אז מה שנרצה לעשות הוא למצוא דרך טובה יותר <strong>להגדיר</strong> את הערכים של אותם {% equation %}a_{ij}^{\left(k\right)}{% endequation %} מלכתחילה. ההגדרה תיראה די משונה אם פשוט אציג אותה, אז בואו נוכיח תוצאה כללית כלשהי קודם.

משהו שלא דיברתי עליו בכלל עד כה בפוסטים הללו הוא שדרך נוחה להתמודד עם מטריצות היא לפעמים לחלק אותן ל<strong>בלוקים</strong>. כל מטריצה ריבועית {% equation %}A{% endequation %} מסדר {% equation %}n\times n{% endequation %} אפשר להציג בתור {% equation %}A=\left(\begin{array}{cc} A_{11} & A_{12}\\ A_{21} & A_{22} \end{array}\right){% endequation %} כך ש-{% equation %}A_{11}{% endequation %} היא מטריצה מסדר {% equation %}k\times k{% endequation %} שכוללת את מה שמקבלים אם מעתיקים מ-{% equation %}A{% endequation %} את כל הכניסות מהצורה {% equation %}a_{ij}{% endequation %} עבור {% equation %}1\le i,j\le k{% endequation %}. גם שאר המטריצות נקבעות בצורה דומה: {% equation %}A_{12}{% endequation %} תהיה מסדר {% equation %}k\times\left(n-k\right){% endequation %}, {% equation %}A_{21}{% endequation %} תהיה מסדר {% equation %}\left(n-k\right)\times k{% endequation %} ו-{% equation %}A_{22}{% endequation %} תהיה מסדר {% equation %}\left(n-k\right)\times\left(n-k\right){% endequation %}, אבל בואו נתמקד לרגע ב-{% equation %}A_{11}{% endequation %}. זו המטריצה

{% equation %}A_{11}=\left(\begin{array}{cccc} a_{11} & a_{12} & \cdots & a_{1k}\\ a_{21} & a_{22} &  & a_{2k}\\ \vdots &  & \ddots & \vdots\\ a_{k1} & a_{k2} & \cdots & a_{kk} \end{array}\right){% endequation %}

מטריצה כזו, שמתקבלת מ-{% equation %}A{% endequation %} על ידי לקיחת {% equation %}k{% endequation %} השורות והעמודות הראשונות ומחיקת כל היתר, נקראת לפעמים <strong>המינור העיקרי</strong> (principle) מסדר {% equation %}k{% endequation %} של המטריצה. אני הולך להניח שהוא הפיך, כלומר {% equation %}\left|A_{11}\right|\ne0{% endequation %}; בהמשך נראה מה קורה כשזה לא המצב (רמז: האלגוריתם שהצגתי קודם עדיין לא שלם). אם הוא לא הפיך, זה נותן לנו פירוק פשוט יחסית של {% equation %}A{% endequation %} למכפלה של שתי מטריצות בלוקים אלכסוניות:

{% equation %}A=\left(\begin{array}{cc} A_{11} & A_{12}\\ A_{21} & A_{22} \end{array}\right)=\left(\begin{array}{cc} A_{11} & 0\\ A_{21} & I \end{array}\right)\left(\begin{array}{cc} I & A_{11}^{-1}A_{12}\\ 0 & A_{22}-A_{21}A_{11}^{-1}A_{12} \end{array}\right){% endequation %}

מה הולך כאן? במבט ראשון זה נראה מבעית, אבל בעצם יש כאן שתי שאלות פשוטות יחסית:

<ul> <li>כשכופלים מטריצות בלוקים, האם חוקי כפל המטריצות הרגילים עדיין תקפים כמו קודם?</li>


<li>אם מניחים שכן, האם החישוב של המכפלה למעלה באמת מחזיר את {% equation %}A{% endequation %}?</li>

</ul>

בואו נענה קודם לשאלה השניה - כמובן. כדי לוודא שאין בעיה עם זה, אני אחשב את כל ארבע הכניסות

<ul> <li>הכניסה של {% equation %}A_{11}{% endequation %}: מתקבלת מכפל השורה הראשונה בעמודה הראשונה, כלומר {% equation %}A_{11}\cdot I+0\cdot0=A_{11}{% endequation %}.</li>


<li>הכניסה של {% equation %}A_{12}{% endequation %}: מתקבלת מכפל השורה הראשונה בעמודה השניה, כלומר {% equation %}A_{11}\cdot\left(A_{11}^{-1}A_{12}\right)+0\cdot\left(A_{22}-A_{21}A_{11}^{-1}A_{12}\right)=A_{12}{% endequation %}</li>


<li>הכניסה של {% equation %}A_{21}{% endequation %}: מתקבלת מכפל השורה השניה בעמודה הראשונה, כלומר {% equation %}A_{21}\cdot I+I\cdot0=A_{21}{% endequation %}.</li>


<li>הכניסה של {% equation %}A_{22}{% endequation %}: מתקבלת מכפלה השורה השניה בעמודה השניה, כלומר {% equation %}A_{21}\cdot A_{11}^{-1}A_{12}+I\cdot A_{22}-A_{21}A_{11}^{-1}A_{12}=A_{22}{% endequation %}</li>

</ul>

כל זה אולי נראה קצת מהונדס מדי כדי שהכל יעבוד, אבל זה כמובן עובד. השאלה היותר מהותית היא למה בכלל מותר לכפול מטריצות בלוקים - וכמו הרבה דברים באלגברה לינארית בסיסית זו תוצאה שאני גם מניח שכולנו מכירים והיא גם די טכנית להוכחה, אז אני לא אוכיח אותה כאן אבל אין כאן חוכמה מיוחדת - אם אתם סקפטיים, נסו להוכיח אותה על שתי מטריצות קטנות קונקרטיות ותראו מה קורה.

עכשיו, מה שנחמד בפירוק המוזר הזה של {% equation %}A{% endequation %} למכפלה של שתי מטריצות בלוקים הוא שזה ממשיך לעבוד כשלוקחים <strong>דטרמיננטה</strong>. כזכור, דטרמיננטה של מכפלה היא מכפלת הדטרמיננטות; וכשיש לנו מטריצת בלוקים {% equation %}\left(\begin{array}{cc} A & 0\\ C & D \end{array}\right){% endequation %} הדטרמיננטה שלה היא {% equation %}\left|A\right|\left|D\right|{% endequation %} (ובאופן דומה כשה-0 הוא במקום {% equation %}C{% endequation %}), כך שנקבל:

{% equation %}\left|A\right|=\left|\left(\begin{array}{cc} A_{11} & 0\\ A_{21} & I \end{array}\right)\right|\left|\left(\begin{array}{cc} I & A_{11}^{-1}A_{12}\\ 0 & A_{22}-A_{21}A_{11}^{-1}A_{12} \end{array}\right)\right|={% endequation %}

{% equation %}\left|A_{11}\right|\left|A_{22}-A_{21}A_{11}^{-1}A_{12}\right|{% endequation %}

עכשיו משתמשים בטריק: כופלים את שני האגפים בסקלר {% equation %}\left|A_{11}\right|^{n-k-1}{% endequation %} ומקבלים

{% equation %}\left|A_{11}\right|^{n-k-1}\left|A\right|=\left|\left|A_{11}\right|\left(A_{22}-A_{21}A_{11}^{-1}A_{12}\right)\right|{% endequation %}

זה יכול להיות די מבלבל, הנה מה שקרה פה: באופן כללי, אם יש לי מטריצה {% equation %}B{% endequation %} ואני כופל שורה כלשהי שלה בסקלר, זה מכפיל את כל הדטרמיננטה באותו סקלר. כדי להוכיח את זה אפשר להשתמש באותה טכניקה שראינו בפוסט הקודם: כפל שורה בסקלר זה כמו כפל במטריצת יחידה {% equation %}I{% endequation %} שאחד מה-1-ים על האלכסון שלה הוחלף בסקלר הבודד {% equation %}\lambda{% endequation %}, והדטרמיננטה של מטריצה כזו היא {% equation %}\lambda{% endequation %} כי היא הרי מכפלת הערכים על האלכסון.

עכשיו, מה קורה אם כופלים את <strong>כל</strong> השורות של {% equation %}B{% endequation %} באותו סקלר, כלומר אם פשוט כפלנו את כל המטריצה {% equation %}B{% endequation %} בסקלר הזה? אם {% equation %}B{% endequation %} היא מטריצה מסדר {% equation %}n\times n{% endequation %} זה אומר שכפלנו את הדטרמיננטה {% equation %}n{% endequation %} פעמים בסקלר {% equation %}\lambda{% endequation %}, אז יש לנו את המשוואה {% equation %}\left|\lambda B\right|=\lambda^{n}\left|B\right|{% endequation %}.

אם נחזור עכשיו למה שעשינו למעלה - יש לנו את המטריצה {% equation %}B=A_{22}-A_{21}A_{11}^{-1}A_{12}{% endequation %}. הסדר של המטריצה הזו הוא {% equation %}\left(n-k\right)\times\left(n-k\right){% endequation %} ולכן {% equation %}\lambda^{n-k}\left|B\right|=\left|\lambda B\right|{% endequation %}. אצלנו {% equation %}\lambda=\left|A_{11}\right|{% endequation %}, ואנחנו מקבלים אותו בחזקת {% equation %}n-k{% endequation %} כי בהתחלה הוא הופיע פעם אחת באגף ימין ואז כפלנו ב-{% equation %}\lambda^{n-k-1}{% endequation %}. זה מסביר את המעבר הזה.

<h2>חלק רביעי, שבו אנו חוזים בשובם של המספרים מהאלגוריתם</h2>

עכשיו הגענו לקאץ': אני אראה שהאיברים של המטריצה {% equation %}\left|A_{11}\right|\left(A_{22}-A_{21}A_{11}^{-1}A_{12}\right){% endequation %} שאליה הגענו הם בעצם ה-{% equation %}a_{ij}^{\left(k\right)}{% endequation %} שמופיעים בשלבי הביניים של האלגוריתם. ראשית, בואו נגדיר את ה-{% equation %}a_{ij}^{\left(k\right)}{% endequation %} הללו במפורש, מה שעד כה נמנעתי מלעשות:

{% equation %}a_{ij}^{\left(k\right)}=\left|\begin{array}{ccccc} a_{11} & a_{12} & \cdots & a_{1k} & a_{1j}\\ a_{21} & a_{22} & \cdots & a_{2k} & a_{2j}\\ \cdots & \cdots & \cdots & \cdots & \cdots\\ a_{k1} & a_{k2} & \cdots & a_{kk} & a_{kj}\\ a_{i1} & a_{i1} & \cdots & a_{ik} & a_{ij} \end{array}\right|{% endequation %} עבור {% equation %}k<i,j\le n{% endequation %}

מה קורה פה? ראשית לוקחים את המטריצה {% equation %}A_{11}{% endequation %} שמתקבלת מ-{% equation %}A{% endequation %} המקורית על ידי לקיחת {% equation %}k{% endequation %} השורות והעמודות הראשונות. עכשיו, מוסיפים שורה חדשה - את שורה מס' {% equation %}i{% endequation %}, כאשר {% equation %}k<i{% endequation %} כלומר זו אחת מהשורות שלא הופיעו במטריצה קודם. אנחנו לא מוסיפים את כל השורה אלא רק את {% equation %}k{% endequation %} העמודות הראשונות שלה. אחר כך אנחנו מוסיפים עמודה {% equation %}j{% endequation %} כך ש-{% equation %}k<j{% endequation %} וגם כאן - לא את כל העמודה, רק את {% equation %}k{% endequation %} השורות הראשונות שלה. לסיום, אחרי שהוספנו את השורה והעמודה עוד נותר מקום ריק אחד בקצה הימני-תחתון של המטריצה, ושם אנחנו שמים את {% equation %}ij{% endequation %}.

<strong>למה</strong> שנגדיר ככה? במאמר המקורי שלו בריס מגיע אל המטריצה הזו בדרך שונה וטכנית יותר - אני דווקא מעדיף את הדרך שבה נוקטים כאן, למרות שהיא נראית כמו קסם (במתמטיקה אין קסמים; כל הגדרה קסומה מגיעה אחרי שמישהו שבר את הראש על הבעיה הרבה זמן וניסה הרבה דברים).

עכשיו, הדטרמיננטה הזו נראית קצת מפחידה אבל כבר ראינו דרך להתמודד איתה - אם שמים לב שיש לנו כאן דטרמיננטה של <strong>מטריצת בלוקים</strong>. הבלוקים הם בדיוק ארבעת הדברים שתיארתי: המטריצה {% equation %}A_{11}{% endequation %} שממנה מתחילים, השורה שהוספתי למטה, העמודה שהוספתי משמאל, וה-{% equation %}a_{ij}{% endequation %} שהוספתי למטה. כלומר יש לנו כאן את מטריצת הבלוקים

{% equation %}B=\left(\begin{array}{cc} B_{11} & B_{12}\\ B_{21} & B_{22} \end{array}\right){% endequation %}

כך ש-{% equation %}B_{11}=A_{11}{% endequation %}, {% equation %}B_{12}=\left(a_{1j},\ldots,a_{kj}\right)^{t},B_{21}=\left(a_{i1},\ldots,a_{ik}\right){% endequation %} ו-{% equation %}B_{22}=\left(a_{ij}\right){% endequation %}.

ראינו את הנוסחה

{% equation %}\left|B\right|=\left|B_{11}\right|\left|B_{22}-B_{21}B_{11}^{-1}B_{12}\right|{% endequation %}

כאן {% equation %}\left|B\right|=a_{ij}^{\left(k\right)}{% endequation %} כי {% equation %}a_{ij}^{\left(k\right)}{% endequation %} הוגדר בתור הדטרמיננטה של המטריצה הזו. קצת יותר מעניין מה זה {% equation %}B_{21}B_{11}^{-1}B_{12}{% endequation %} - זה כפל של מטריצה ({% equation %}A_{11}^{-1}{% endequation %}) במטריצת עמודה מימין ומטריצת שורה משמאל - התוצאה היא סקלר, וחישוב ישיר על פי ההגדרה של כפל מטריצות נותן ש-

{% equation %}B_{21}B_{11}^{-1}B_{12}=\sum_{r=1}^{k}\sum_{s=1}^{k}a_{ir}\left[A_{11}^{-1}\right]_{rs}a_{sj}{% endequation %}

ולכן משילוב כל הדברים הללו אנחנו מקבלים

{% equation %}a_{ij}^{\left(k\right)}=\left|A_{11}\right|\left(a_{ij}-\sum_{r=1}^{k}\sum_{s=1}^{k}a_{ir}\left[A_{11}^{-1}\right]_{rs}a_{sj}\right){% endequation %}

מה שיש לנו באגף שמאל הוא בדיוק את האיבר ה-{% equation %}ij{% endequation %} של המטריצה {% equation %}\left|A_{11}\right|\left(A_{22}-A_{21}A_{11}^{-1}A_{12}\right){% endequation %}, אם כי צריך קצת להיזהר עם האינדקסים כדי לראות את זה כי המטריצה הזו <strong>מתחילה</strong> לא מהאינדקס {% equation %}1,1{% endequation %} אלא מהאינדקס {% equation %}k+1,k+1{% endequation %}.

איך זה עוזר לנו? ובכן, קודם כל שימו לב שכמו שאמרתי קודם - המינורים העיקריים של {% equation %}A{% endequation %} מתקבלים ככה. ממש על פי ההגדרה, מתקיים {% equation %}\left|A_{11}\right|=a_{kk}^{\left(k-1\right)}{% endequation %}, כי {% equation %}A_{11}{% endequation %} מתקבלת מלקיחת {% equation %}k{% endequation %} השורות והעמודות הראשונות ואילו המטריצה שבה משתמשים לחישוב {% equation %}a_{kk}^{\left(k-1\right)}{% endequation %} מתקבלת מלקיחת {% equation %}k-1{% endequation %} השורות והעמודות הראשונות ואז הוספה אליהן של השורה והעמודה הבאות בתור.

לכן אני יכול ללכת אל הנוסחה שהוכחתי קודם:

{% equation %}\left|A_{11}\right|^{n-k-1}\left|A\right|=\left|\left|A_{11}\right|\left(A_{22}-A_{21}A_{11}^{-1}A_{12}\right)\right|{% endequation %}

ולהציב בתוכה את {% equation %}\left|A_{11}\right|=a_{kk}^{\left(k-1\right)}{% endequation %} מצד אחד, ואילו בצד השני יש לנו כאמור את המטריצה {% equation %}\left|A_{11}\right|\left(A_{22}-A_{21}A_{11}^{-1}A_{12}\right){% endequation %} שהאיברים שלה הם בדיוק ה-{% equation %}a_{ij}^{\left(k\right)}{% endequation %} עבור {% equation %}k<i,j\le n{% endequation %}, ולכן קיבלנו את הנוסחה

{% equation %}\left|A\right|\left[a_{kk}^{\left(k-1\right)}\right]^{n-k-1}=\left|\begin{array}{ccc} a_{k+1,k+1}^{\left(k\right)} & \cdots & a_{k+1,n}^{\left(k\right)}\\ \cdots & \cdots & \cdots\\ a_{n,k+1}^{\left(k\right)} & \cdots & a_{n,n}^{\left(k\right)} \end{array}\right|{% endequation %}

את הנוסחה הזו הוכחנו לכל מטריצה {% equation %}A{% endequation %} (עם ההנחה שהמינור העיקרי שלה, מה שסימנתי ב-{% equation %}A_{11}{% endequation %}, הוא מדטרמיננטה שונה מאפס), אז אפשר להשתמש בה גם עבור המטריצה שאיתה הגדרנו את {% equation %}a_{ij}^{\left(k\right)}{% endequation %}, כלומר המטריצה שמורכבת מהמינור העיקרי {% equation %}A_{11}{% endequation %} ואז עוד שורה ועמודה. צריך קצת להיזהר עם האינדקסים: עד עכשיו השתמשתי ב-{% equation %}k{% endequation %} כדי לציין אינדקס כלשהו, {% equation %}1\le k\le n{% endequation %} שמתאים למינור העיקרי שבו מטפלים באותו הרגע, אבל עכשיו כשאני רוצה להשתמש בנוסחה הזו כדי לטפל ב-{% equation %}a_{ij}^{\left(k\right)}{% endequation %} ולכן יש לי חופש בחירה של המינור העיקרי <strong>שלו</strong> שאנחנו בוחרים, צריך להשתמש באינדקס אחר - במאמר שלו ברייס משתמש ב-{% equation %}l{% endequation %}, ואז מקבלים

{% equation %}a_{ij}^{\left(k\right)}\left[a_{ll}^{\left(l-1\right)}\right]^{\left(k+1\right)-l-1}=\left|\begin{array}{cccc} a_{l+1,l+1}^{\left(l\right)} & \cdots & a_{l+1,k}^{\left(l\right)} & a_{l+1,j}^{\left(l\right)}\\ \cdots & \cdots & \cdots & \cdots\\ a_{k,l+1}^{\left(l\right)} & \cdots & a_{k,k}^{\left(l\right)} & a_{k,j}^{\left(l\right)}\\ a_{i,l+1}^{\left(l\right)} & \cdots & a_{i,k}^{\left(l\right)} & a_{i,j}^{\left(l\right)} \end{array}\right|{% endequation %}

הסיבה לכך שיש {% equation %}k+1{% endequation %} בחזקה באגף שמאל הוא שזה הסדר של המטריצה שמגדירה את {% equation %}a_{ij}^{\left(k\right)}{% endequation %} (כי לקחנו מטריצה {% equation %}k\times k{% endequation %} והוספנו לה שורה ועמודה). השינוי באיך שאני מציג את האיברים בתוך הדטרמיננטה באגף ימין (עוד שורה ועמודה) הוא רק כדי שיהיה יותר קל להבין מה קורה, בגלל שהמבנה של השורה והעמודה האחרונות במטריצה הוא שונה מאשר עבור יתר הכניסות.

עכשיו, תחת ההנחה שלנו על כך שהדטרמיננטה של המינורים העיקריים היא לא אפס אנחנו מקבלים ש-{% equation %}a_{ll}^{\left(l-1\right)}{% endequation %} הוא לא אפס (כי הוא שווה למינור עיקרי שכזה) ולכן אפשר לחלק בו ולקבל

{% equation %}a_{ij}^{\left(k\right)}=\frac{1}{\left[a_{ll}^{\left(l-1\right)}\right]^{k-l}}\left|\begin{array}{cccc} a_{l+1,l+1}^{\left(l\right)} & \cdots & a_{l+1,k}^{\left(l\right)} & a_{l+1,j}^{\left(l\right)}\\ \cdots & \cdots & \cdots & \cdots\\ a_{k,l+1}^{\left(l\right)} & \cdots & a_{k,k}^{\left(l\right)} & a_{k,j}^{\left(l\right)}\\ a_{i,l+1}^{\left(l\right)} & \cdots & a_{i,k}^{\left(l\right)} & a_{i,j}^{\left(l\right)} \end{array}\right|{% endequation %}

וזה נותן לנו דרך לחשב רקורסיבית את ה-{% equation %}a_{ij}^{\left(k\right)}{% endequation %}-ים! נזכיר את תנאי ההתחלה שלנו:

{% equation %}a_{00}^{\left(-1\right)}=1,a_{ij}^{\left(0\right)}=a_{ij}{% endequation %}

ובנוסחה למעלה, כדי לצמצם כמה שרק ניתן את הגודל של הדטרמיננטה אפשר לבחור {% equation %}l=k-1{% endequation %} ולקבל

{% equation %}a_{ij}^{\left(k\right)}=\frac{1}{a_{k-1,k-1}^{\left(k-2\right)}}\left|\begin{array}{cc} a_{kk}^{\left(k-1\right)} & a_{kj}^{\left(k-1\right)}\\ a_{ik}^{\left(k-1\right)} & a_{ij}^{\left(k-1\right)} \end{array}\right|=\frac{a_{ij}^{\left(k-1\right)}a_{kk}^{\left(k-1\right)}-a_{ik}^{\left(k-1\right)}a_{kj}^{\left(k-1\right)}}{a_{k-1,k-1}^{\left(k-2\right)}}{% endequation %}

כשהשוויון האחרון נובע פשוט מחישוב ישיר של הדטרמיננטה. זה משלים את ההוכחה, כי קיבלנו בדיוק את הנוסחה שהופיעה באלגוריתם, ועכשיו אנחנו גם מבינים למה החלוקה ב-{% equation %}a_{k-1,k-1}^{\left(k-2\right)}{% endequation %} "מצליחה" ואנחנו מקבלים מספר שלם - כי {% equation %}a_{ij}^{\left(k\right)}{% endequation %} מלכתחילה הוגדר בתור דטרמיננטה של מטריצה שמכילה רק מספרים שלמים (זאת בהנחה שהמטריצה המקורית הכילה רק שלמים) ולכן אם יש שבר ששווה לו, המכנה חייב לחלק את המונה.

<h2>חלק חמישי ואחרון, שבו אנו מגיעים לגרסה המלאה של האלגוריתם</h2>

יפה, אז ראינו את ההוכחה לכך שהאלגוריתם הבא עובד:

<ul> <li>אתחל את המשתנים {% equation %}a_{ij}^{\left(0\right)}=a_{ij}{% endequation %} לכל {% equation %}1\le i,j\le n{% endequation %} ואת המשתנה המיוחד {% equation %}a_{00}^{\left(-1\right)}=1{% endequation %}.</li>


<li>לכל {% equation %}k=1,2,\ldots,n-1{% endequation %}:</li>
<ul>
<li>לכל {% equation %}k+1\le i,j\le n{% endequation %}, קבעו {% equation %}a_{ij}^{\left(k\right)}\leftarrow\frac{a_{ij}^{\left(k-1\right)}a_{kk}^{\left(k-1\right)}-a_{ik}^{\left(k-1\right)}a_{kj}^{\left(k-1\right)}}{a_{k-1,k-1}^{\left(k-2\right)}}{% endequation %}</li>
</ul>
</ul>


<li>החזירו את {% equation %}a_{nn}^{\left(n-1\right)}{% endequation %}</li>

עכשיו, מהנוסחה הזו ברור שאם אנחנו בשלב {% equation %}k{% endequation %}, אז כל הערכים במטריצה שהשורה או העמודה שלהם היא לכל היותר {% equation %}k{% endequation %} כבר לא מעניינים אותנו, למעט האיבר במקום {% equation %}k-1,k-1{% endequation %} - אבל גם עבורו, אנחנו נצטרך רק <strong>לקרוא</strong> את הערך שלו ולא נשנה אותו יותר. זה אומר שאם אנחנו מקבלים את המטריצה כקלט, אז בשביל לחסוך מקום אפשר לשמור את ערכי הביניים <strong>בתוכה</strong> (אם לא מפריע לנו שהיא תשתנה; אם לא נרצה שהפונקציה תשפיע על המטריצה המקורית יהיה צורך ליצור עותק שלה, אבל גם אז עדיף עותק אחד על סביבות {% equation %}n{% endequation %} עותקים כאלו).

אם נוקטים בגישה הזו, זה מה שהאלגוריתם הופך להיות:

<ul> <li>אתחלו את המשתנה {% equation %}A_{00}=1{% endequation %}</li>


<li>לכל {% equation %}k=1,2,\ldots,n-1{% endequation %}:</li>
<ul>

<li>לכל {% equation %}k+1\le i,j\le n{% endequation %}, קבעו {% equation %}A_{ij}\leftarrow\frac{A_{ij}A_{kk}-A_{ik}A_{kj}}{A_{k-1,k-1}}{% endequation %}</li>
</ul>
</ul>


<li>החזירו את {% equation %}A_{n-1,n-1}{% endequation %}</li>

בפועל כשכותבים קוד לא כזה כיף להוסיף משתנה {% equation %}A_{00}{% endequation %} כי צריך קוד מיוחד לטפל בו ולא במטריצה {% equation %}A{% endequation %}, ולכן הרבה יותר פשוט לבדוק אם {% equation %}k=1{% endequation %} ואם כן - פשוט לוותר על פעולת החילוק באיטרציה הזו של האלגוריתם. בקוד שאצרף עוד רגע אפשר יהיה לראות את זה.

יש רק דבר אחד שטרם התייחסתי אליו - מה קורה אם אחד מהמינורים העיקריים הוא עם דטרמיננטה 0? במקרה הזה, החישוב יניב בשלב כלשהו {% equation %}A_{kk}=0{% endequation %} ואי אפשר יהיה לחלק בו. בסיטואציה הזו עושים דבר דומה למה שהיה באלגוריתם ה"רגיל" לדטרמיננטה - מחפשים בעמודה ה-{% equation %}k{% endequation %}-ית החל מהשורה ה-{% equation %}k+1{% endequation %} כניסה ששונה מאפס, ואם נמצאה כזו - מחליפים את השורות ומכפילים את הסימן של הדטרמיננטה ב-{% equation %}-1{% endequation %}. זה האלגוריתם המלא (שימו לב שבפייתון // מייצג חילוק בשלמים - כלומר, חילוק שמתעלם מהשארית, אם יש כזו, ומחזיר רק את המנה השלמה):

{% highlight python %}
def bareiss_det(A):
    sign = 1
    n = len(A)
    for k in range(n-1):
        if A[k][k] == 0:
            for i in range(k+1,n):
                if A[i][k] != 0:
                    A[k], A[i] = A[i], A[k]
                    sign *= -1
                    break
            if A[k][k] == 0:
                return 0
        for i in range(k+1, n):
            for j in range(k+1, n):
                A[i][j] = (A[i][j] * A[k][k] - A[i][k] * A[k][j])
                if k != 0:
                     A[i][j] = A[i][j] // A[k-1][k-1]
            A[i][k]=0
    return sign * A[-1][-1]
{% endhighlight %}
