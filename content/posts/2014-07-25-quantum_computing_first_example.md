---
id: 3159
title: "חישוב קוונטי - דוגמה ראשונה"
date: 2014-07-25 08:14:31
layout: post
categories: 
  - פיזיקה
  - חישוב קוונטי
tags: 
  - חישוב קוונטי
---
אני רוצה להתחיל עם הדגמה לאופן שבו חישוב קוונטי מסוגל לסייע בתקשורת. זו דוגמה טובה כי מצד אחד קורה בה "קסם" של ממש: אנחנו מצליחים לעשות משהו שמבחינה "קלאסית" הוא פשוט בלתי אפשרי. מצד שני, אנחנו גם רואים בדיוק עד כמה המשהו הזה הוא מוגבל ולא מתאים לרושם שעשוי להיווצר מתיאורי מדע פופולרי. ואנחנו מקבלים הזדמנות לראות את המתמטיקה של הפוסט הקודם בפעולה.

מה שנסתכל עליו הוא מעין משחק די מוזר שבו משתתפים שני שחקנים: אליס ובוב. אליס ובוב נפגשים, מדברים, מחליטים על אסטרטגיה, מחליפים ביניהם חפצים וכל מה שהם רק רוצים, ואז עולים על חלליות ונוסעים לשני קצוות היקום (נאמר, מרחק של שנת אור ביניהם). עכשיו, מנהל המשחק מגריל שני ביטים {% equation %}x,y{% endequation %} באקראי. לאליס הוא נותן את {% equation %}x{% endequation %} ולבוב הוא נותן את {% equation %}y{% endequation %} בו זמנית (אני אתחמק כאן מהשאלה מה זה "בו זמנית" בהקשר הזה). לשניהם יש שעה לעשות דברים, ולאחר מכן אליס שולחת למנהל המשחק ביט {% equation %}a{% endequation %} ובוב שולח למנהל המשחק ביט {% equation %}b{% endequation %}. המטרה? שיתקיים {% equation %}a\oplus b=x\wedge y{% endequation %} (כאשר {% equation %}a\oplus b{% endequation %} הוא חיבור מודולו 2 ובעברית יפה XOR, כלומר הוא 0 אם {% equation %}a=b{% endequation %} ו-{% equation %}1{% endequation %} אם {% equation %}a\ne b{% endequation %}, ואילו {% equation %}x\wedge y{% endequation %} הוא AND, כלומר שווה ל-0 אלא אם {% equation %}x=y=1{% endequation %}, ואז הוא שווה 1). במילים אחרות, המטרה היא שאליס ובוב יגידו את אותו הביט, אלא אם {% equation %}x=y=1{% endequation %} ואז דווקא רוצים שיענו תשובות הפוכות.

המשחק הוא בבירור הסתברותי. השאלה היא רק מה הסתברות ההצלחה של אליס ובוב במשחק הזה. כל עוד אנחנו נמצאים בפיזיקה קלאסית (פלוס תורת היחסות הפרטית), המרחק שבין אליס ובוב הוא גדול כל כך עד שמסגרת השעה שיש להם שום מידע לא יכול לעבור מאליס אל בוב וההפך, ולכן הם יכולים לעבוד רק על בסיס אסטרטגיה שהם הסכימו עליה מראש. זה לא מסובך (אבל לא אעשה את זה כרגע) להוכיח שהאסטרטגיה הטובה ביותר נותנת הסתברות הצלחה של {% equation %}\frac{3}{4}{% endequation %} והיא מאוד פשוטה: גם אליס וגם בוב יענו תמיד {% equation %}0{% endequation %} (ולכן הסיטואציה היחידה שבה הם טועים היא זו שבה {% equation %}x=y=1{% endequation %}, מה שקורה בהסתברות {% equation %}\frac{1}{4}{% endequation %}).

האם תורת הקוונטים יכולה לשפר את סיכויי ההצלחה של אליס ובוב? ובכן, כן.

ארחיב על הרעיון הכללי בהמשך, אבל בינתיים רק אציין את העובדות הבאות: ראשית, מערכת קוונטית לא חייבת להיות כולה באותו המקום. אם יש לנו מערכת של שני קיוביטים, אין מניעה עקרונית שאחד הקיוביטים יהיה עם אליס והשני יהיה עם בוב, למרות המרחק הפיזי הגדול בין אליס ובוב. שנית, מדידה של המערכת משפיעה על המערכת "בבת אחת" עבור כל מי שמחזיק בחלק מהמערכת; דהיינו, אם אליס מודדת את הביט שלה, המערכת כולה מושפעת מייד וגם בוב "ירגיש" את ההשפעה הזו, עד כמה שהוא יכול להרגיש אותה בהתחשב בכך שאין לו את הביט שאליס מדדה.

אז מה שקורה הוא הדבר הבא: ראשית, כשאליס ובוב נפגשים כדי לקבוע אסטרטגיה ולהחליף חפצים, הם משתפים ביניהם מערכת קוונטית של שני קיוביטים שנמצאת במצב הבא: {% equation %}\left|00\right\rangle +\left|11\right\rangle {% endequation %}. אני מזכיר שהסימון הזה הוא דרך מקוצרת לכתוב {% equation %} \frac{\left|00\right\rangle +\left|11\right\rangle }{\sqrt{2}}{% endequation %} שהוא בתורו דרך מקוצרת לכתוב את הצירוף הלינארי הכללי {% equation %}\frac{1}{\sqrt{2}}\cdot\left|00\right\rangle +0\cdot\left|10\right\rangle +0\cdot\left|01\right\rangle +\frac{1}{\sqrt{2}}\cdot\left|11\right\rangle {% endequation %} שהוא בתורו דרך מקוצרת לכתוב {% equation %}\frac{1}{\sqrt{2}}\cdot\left|0\right\rangle \otimes\left|0\right\rangle +0\cdot\left|1\right\rangle \otimes\left|0\right\rangle +0\cdot\left|0\right\rangle \otimes\left|1\right\rangle +\frac{1}{\sqrt{2}}\cdot\left|1\right\rangle \otimes\left|1\right\rangle {% endequation %}. נראה לי שהכתיב של {% equation %}\left|00\right\rangle +\left|11\right\rangle {% endequation %} עדיף. יש מישהו בקהל שרוצה להעיר עוד הערות על ענייני סימון?

המצב הקוונטי {% equation %}\left|00\right\rangle +\left|11\right\rangle {% endequation %} הוא מעניין מכיוון שהוא מצביע על "תיאום" בין שני הקיוביטים שמעורבים בו. אם נמדוד את אחד מהביטים ונגרום לו לקרוס, זה יגרום גם לביט השני לקרוס לאותו ערך שנמדד כמו של הביט הראשון. זה יוצר מעין <strong>תיאום בו זמני</strong> בין אליס ובוב, אפילו אם הם נמצאים במרחק גדול זו מזה. על ההשלכות הפילוסופיות-פיזיקליות של זה אדבר בהמשך, בינתיים אני רוצה להסביר איך זה עוזר לנו במשחק.

האינטואיציה הראשונית היא שאליס תוכל להעביר לבוב את המידע על הביט {% equation %}x{% endequation %} שקיבלה. איך? אם הביט הוא 0 היא תפעיל טרנספורמציה על המצב הקוונטי שלה שתהפוך אותו ל-{% equation %}\left|00\right\rangle {% endequation %}, ואחרת היא תפעיל עליו טרנספורמציה שתהפוך אותו ל-{% equation %}\left|11\right\rangle {% endequation %}. בוב ימדוד את המצב שלו, יקבל תשובה בודאות של 100 אחוז, ויענה בהתאם. זה רעיון טוב, אבל הוא מתעלם מכך שלאליס אין ביד את כל המערכת הקוונטית; יש לה רק את הקיוביט שלה, ולכן היא מסוגלת לבצע רק עליו פעולות.

עכשיו אני הולך להתחיל להיות טכני, ולכן לפני כן אני אגלה לכם מה בדיוק עושים, כי זה באמת פשוט: אליס ובוב בודקים את הביטים שקיבלו. מי שקיבל 0 לא עושה כלום. מי שקיבל 1 מפעיל על הקיוביט שלו טרנספורמציה מסויימת שאתאר בהמשך (לכל אחד מהם יש טרנספורמציה אחרת). אחר כך הם מודדים את הקיוביטים שלהם ועונים לפי תוצאת המדידה. זה הכל; העיקר הוא כמובן בכך שהטרנספורמציה שהם ביצעו על הקיוביטים שלהם משפיעה איכשהו על תוצאת המדידה. כדי להבין איך נצטרך להיכנס לפרטים. אעיר מראש שפרט אחד שאני <strong>לא</strong> הולך להיכנס אליו בכלל הוא האופן שבו סדר הפעולות משפיע על החישוב - הוא לא, אבל כדי לראות את זה הפוסט יצטרך להתנפח עם עוד חישובים שמגיעים לאותה התוצאה. אם זה מפריע לכם אתם יכולים לבצע את הבדיקה בעצמכם.

בואו נתאר שניה איך מבצעים פעולות על מערכת קוונטית. נתחיל עם מערכת של קיוביט בודד, עם מצבי בסיס {% equation %}\left|0\right\rangle {% endequation %} ו-{% equation %}\left|1\right\rangle {% endequation %}. כל פעולה (שאינה מדידה) שניתן לבצע על המערכת ניתנת לתיאור על ידי מטריצה {% equation %}2\times2{% endequation %} {% equation %}A{% endequation %} שהיא <strong>אוניטרית</strong>, כלומר {% equation %}AA^{*}=I{% endequation %} (והמשמעות: {% equation %}A{% endequation %} משמרת נורמה של וקטורים שהיא פועלת עליהם). דוגמה קלאסית לטרנספורמציה אוניטרית על מרחב ממימד 2 היא <strong>סיבוב</strong>. סיבוב בזווית של {% equation %}\theta {% endequation %} מעלות מתואר על ידי המטריצה {% equation %}A=\left[\begin{array}{cc}\cos\theta & -\sin\theta\\\sin\theta & \cos\theta\end{array}\right]{% endequation %}. דרך אחרת, שקולה, לתאר את {% equation %}A{% endequation %} היא לתאר את האופן שבו היא פועלת על מצבי הבסיס - לאן היא שולחת אותם:

{% equation %}\left|0\right\rangle \mapsto\cos\theta\left|0\right\rangle +\sin\theta\left|1\right\rangle {% endequation %}

{% equation %}\left|1\right\rangle \mapsto\cos\theta\left|1\right\rangle -\sin\theta\left|0\right\rangle {% endequation %}

אם, למשל, היינו מפעילים את הטרנספורמציה הזו עם זווית של {% equation %}\theta=-\frac{\pi}{4}{% endequation %} על המצב הקוונטי, היינו מקבלים את הדבר הבא (זכרו ש-{% equation %}\cos\theta=\frac{1}{\sqrt{2}}{% endequation %} ו-{% equation %}\sin\theta=-\frac{1}{\sqrt{2}}{% endequation %} במקרה זה):

{% equation %}\frac{\left|0\right\rangle +\left|1\right\rangle }{\sqrt{2}}\mapsto\frac{\left(\left|0\right\rangle -\left|1\right\rangle \right)+\left(\left|0\right\rangle +\left|1\right\rangle \right)}{2}=\left|0\right\rangle {% endequation %}

כלומר, הטרנספורמציה הזו אכן מסוגלת לקחת מצב "מעורבב" של {% equation %}\left|0\right\rangle +\left|1\right\rangle {% endequation %} ולהעביר אותו למצב "טהור" (בדומה גם ל-{% equation %}\left|1\right\rangle {% endequation %} אפשר להגיע עם טרנספורמציה אחרת). אבל זה, כאמור, במערכת של קיוביט אחד. במערכת של שני הקיוביטים שלנו אם אליס תפעיל סיבוב ב-{% equation %}\theta{% endequation %} מעלות על הקיוביט שלה, הפעולה ה"כללית" היא בעצם שילוב של שתי פעולות: סיבוב של הקיוביט של אליס, והשארה ללא שינוי של הקיוביט של בוב, מה שמתואר על ידי המטריצה {% equation %}I{% endequation %}. שתי אלו הן מטריצות {% equation %}2\times2{% endequation %} - איך מקבלים מהן את המטריצה {% equation %}4\times4{% endequation %} שמתארת את הפעולה של אליס על המרחב של שני הקיוביטים?

התשובה פשוטה: מכפלת קרונקר של המטריצות. מכפלת קרונקר, כזכור, פירושו לקחת את אחת המטריצות ולדחוף עותק שלה לתוך כל כניסה במטריצה השניה, תוך שהמטריצה מוכפלת בסקלר שהוא הערך של הכניסה של המטריצה השניה. במקרה שלנו אנחנו לוקחים את המטריצה {% equation %}\left[\begin{array}{cc}\cos\theta & -\sin\theta\\\sin\theta & \cos\theta\end{array}\right]{% endequation %} ודוחפים אותה לתוך המטריצה {% equation %}\left[\begin{array}{cc}1 & 0\\0 & 1\end{array}\right]{% endequation %}. נקבל את המטריצה

{% equation %}\left[\begin{array}{cccc}\cos\theta & -\sin\theta & 0 & 0\\\sin\theta & \cos\theta & 0 & 0\\0 & 0 & \cos\theta & -\sin\theta\\0 & 0 & \sin\theta & \cos\theta\end{array}\right]{% endequation %}

המטריצה הזו מבוססת על הנחה כלשהי שלי על הסדר של אברי הבסיס במכפלה הטנזורית - ספציפית, שהוא זה: {% equation %}\left|00\right\rangle ,\left|10\right\rangle ,\left|01\right\rangle ,\left|11\right\rangle {% endequation %}. כלומר, שאנחנו כל פעם מתקדמים קודם כל על פי הרכיב הראשון ואז הרכיב השני.

אם אני אנסה לכתוב את הפעולה הזו על פי מה שהיא מעוללת לוקטורים, אני אקבל את זה:

{% equation %}\left|00\right\rangle \mapsto\cos\theta\left|00\right\rangle +\sin\theta\left|10\right\rangle {% endequation %}

{% equation %}\left|11\right\rangle \mapsto\cos\theta\left|11\right\rangle -\sin\theta\left|01\right\rangle {% endequation %}

{% equation %}\left|10\right\rangle \mapsto\cos\theta\left|10\right\rangle -\sin\theta\left|00\right\rangle {% endequation %}

{% equation %}\left|01\right\rangle \mapsto\cos\theta\left|01\right\rangle +\sin\theta\left|11\right\rangle {% endequation %}

אז אם אליס תפעיל סיבוב בזווית {% equation %}\theta{% endequation %} על המערכת במצב {% equation %}\left|00\right\rangle +\left|11\right\rangle {% endequation %} היא תעביר אותה למצב {% equation %}\cos\theta\left|00\right\rangle +\sin\theta\left|10\right\rangle -\sin\theta\left|01\right\rangle +\cos\theta\left|11\right\rangle {% endequation %}.

הבנו איך נראות טרנספורמציות אוניטריות שמופעלת על קיוביט בודד ברמת ההשפעה שלהן על כל המערכת; עכשיו בואו נראה מה קורה עם מדידה של קיוביט בודד ואיך היא משפיעה על כל המערכת. המדידה שלנו תהיה ביחס לבסיס הסטנדרטי, כלומר הטלה לתת-המרחב שנפרש על ידי {% equation %}\left|0\right\rangle {% endequation %} או לתת-המרחב שנפרש על ידי {% equation %}\left|1\right\rangle {% endequation %}. את ההטלה הראשונה אפשר לתאר על ידי הטרנספורמציה

{% equation %}\left|0\right\rangle \mapsto1\cdot\left|0\right\rangle +0\cdot\left|1\right\rangle {% endequation %}

{% equation %}\left|1\right\rangle \mapsto0\cdot\left|0\right\rangle +0\cdot\left|1\right\rangle {% endequation %}

שהמטריצה שלה היא {% equation %}\left[\begin{array}{cc}1 & 0\\0 & 0\end{array}\right]{% endequation %} (שימו לב - לא מטריצה אוניטרית!). אחרי מכפלה טנזורית עם {% equation %}I{% endequation %} נקבל את המטריצה

{% equation %}\left[\begin{array}{cccc}1 & 0 & 0 & 0\\0 & 0 & 0 & 0\\0 & 0 & 1 & 0\\0 & 0 & 0 & 0\end{array}\right]{% endequation %}

שמתאימה לטרנספורמציה

{% equation %}\left|00\right\rangle \mapsto\left|00\right\rangle {% endequation %}

{% equation %}\left|11\right\rangle \mapsto0{% endequation %}

{% equation %}\left|10\right\rangle \mapsto0{% endequation %}

{% equation %}\left|01\right\rangle \mapsto\left|01\right\rangle {% endequation %}

שאפשר לסמן יותר בקלות בתור {% equation %}\left|00\right\rangle \left\langle 00\right|+\left|01\right\rangle \left\langle 01\right|{% endequation %}.

כלומר (וזה היה כמובן צפוי לגמרי אבל טוב היה לראות את זה בעיניים) קיבלנו את ההטלה לתת-המרחב שנפרש על ידי {% equation %}\left|00\right\rangle {% endequation %} ו-{% equation %}\left|01\right\rangle {% endequation %}, כלומר המצבים שבהם הביט שמדדנו הוא 0. אני מניח שאתם יכולים לנחש איך נראה אופרטור המדידה שהוא הטלה לתת-המרחב שנפרש על ידי {% equation %}\left|1\right\rangle {% endequation %} כשמרחיבים אותו למערכת של שני הקיוביטים.

עכשיו בואו נעבור לאקשן. ראשית, מה האלגוריתם? אליס ובוב מקבלים ביטים {% equation %}x,y{% endequation %} כקלט. אם אליס קיבלה {% equation %}x=0{% endequation %} היא לא עושה כלום; אם היא קיבלה {% equation %}1{% endequation %} היא מפעילה על הקיוביט שלה טרנספורמציית <strong>סיבוב</strong> בזווית {% equation %}\theta=\frac{\pi}{8}{% endequation %}. ומה בוב עושה? אם {% equation %}y=0{% endequation %}, כלום; אם {% equation %}y=1{% endequation %}, סיבוב בזווית {% equation %}\theta=-\frac{\pi}{8}{% endequation %} (שימו לב למינוס, הוא חשוב!). אחר כך שניהם מודדים את הקיוביט שלהם ועונים כמו תוצאת המדידה.

כעת, מה המדידות של אליס ובוב יכולות להחזיר אם הביטים של שניהם היו 0 ולכן הם לא נגעו במערכת? כמובן שהאינטואיציה היא ששניהם יענו אותו דבר, כי לא משנה לאיזה ערך המערכת קורסת, שני הקיוביטים יהיו מתואמים.

הבה ונוכיח את האינטואיציה הזו. נאמר שאליס מודדת ראשונה את הקיוביט שלה. המערכת כרגע במצב {% equation %}\left|00\right\rangle +\left|11\right\rangle {% endequation %}, אבל זה סימון מקוצר שמשמיט את קבוע הנורמליזציה של הקיוביטים ומכיוון שאנחנו הולכים לבצע מדידה עדיף שלא נשכח את הקבוע הזה. אז נסמן את מצב המערכת בתור {% equation %}\frac{\left|00\right\rangle +\left|11\right\rangle }{\sqrt{2}}{% endequation %}. או שנקרוס בהסתברות {% equation %}\left|\left(\left|00\right\rangle \left\langle 00\right|+\left|01\right\rangle \left\langle 01\right|\right)\frac{\left|00\right\rangle +\left|11\right\rangle }{\sqrt{2}}\right|^{2}=\left|\frac{\left|00\right\rangle }{\sqrt{2}}\right|^{2}=\frac{1}{2}{% endequation %} למצב {% equation %}\left|00\right\rangle {% endequation %} או שנקרוס בהסתברות {% equation %}\frac{1}{2}{% endequation %} למצב {% equation %}\left|11\right\rangle {% endequation %}.

נניח שקרסנו ל-{% equation %}\left|00\right\rangle {% endequation %}, מה יקרה עם בוב? ובכן, אתם יכולים לעשות את החישוב בצד אבל זה מיותר; די ברור שבוב יקבל 0. לכן אליס ובוב יענו שניהם 0 כאן וינצחו (זכרו - הם צריכים לענות שונה רק אם שניהם קיבלו את הקלט 1, וכאן שניהם קיבלו את הקלט 0). באופן דומה גם קריסה ל-{% equation %}\left|11\right\rangle {% endequation %} תוביל לכך שגם אליס וגם בוב יענו 1.

אז במקרה הקל טיפלנו. כעת, מה קורה אם אליס מקבלת 1 ובוב לא? ובכן, ראינו כבר שאליס תבצע טרנספורמציית סיבוב שתעביר את המערכת למצב {% equation %}\cos\frac{\pi}{8}\left|00\right\rangle +\sin\frac{\pi}{8}\left|10\right\rangle -\sin\frac{\pi}{8}\left|01\right\rangle +\cos\frac{\pi}{8}\left|11\right\rangle {% endequation %}. עכשיו, בואו נמדוד! ראשית, הטלה על {% equation %}\left|0\right\rangle {% endequation %} תצליח בהסתברות:

{% equation %}\left|\frac{1}{\sqrt{2}}\left(\cos\frac{\pi}{8}\left|00\right\rangle +\sin\frac{\pi}{8}\left|10\right\rangle -\sin\frac{\pi}{8}\left|01\right\rangle +\cos\frac{\pi}{8}\left|11\right\rangle \right)\left(\left|00\right\rangle \left\langle 00\right|+\left|01\right\rangle \left\langle 01\right|\right)\right|^{2}={% endequation %}

{% equation %}\left|\frac{1}{\sqrt{2}}\left(\cos\frac{\pi}{8}\left|00\right\rangle -\sin\frac{\pi}{8}\left|01\right\rangle \right)\right|^{2}=\frac{1}{2}\left(\cos^{2}\frac{\pi}{8}+\sin^{2}\frac{\pi}{8}\right)=\frac{1}{2}{% endequation %}

רגע, מה? שוב קיבלנו {% equation %}\frac{1}{2}{% endequation %}? אחרי כל המהומה שעשינו? איך זה ייתכן? איך זה עזר לנו? ובכן, בואו נראה מה קורה עכשיו. בהסתברות {% equation %}\frac{1}{2}{% endequation %} אנחנו קורסים, אבל לאיזה מצב? לא למצב {% equation %} \left|00\right\rangle {% endequation %} אלא למצב {% equation %}\cos\frac{\pi}{8}\left|00\right\rangle -\sin\frac{\pi}{8}\left|01\right\rangle {% endequation %} - מצב שמנקודת מבטו של בוב, שרואה רק את הקיוביט השני, נראה כמו {% equation %}\cos\frac{\pi}{8}\left|0\right\rangle -\sin\frac{\pi}{8}\left|1\right\rangle {% endequation %} - במילים אחרות, זה נראה לו כאילו מישהו סובב את הקיוביט שלו ב-{% equation %}-\frac{\pi}{8}{% endequation %}. שימו לב מה קרה: אליס סובבה את הקיוביט <strong>שלה</strong>, אבל בגלל התיאום בין הקיוביטים, אחרי המדידה מה שיש לבוב ביד היא מערכת שבה הקיוביט <strong>שלו</strong> מסובב. עכשיו, בוב כמובן לא "רואה" שהקיוביט שלו מסובב כי הוא לא יכול לדעת את המקדמים של המערכת שלו; כל מה שהוא יכול לעשות הוא לבצע בעצמו מדידה. מה התוצאות האפשריות של המדידה? או, עכשיו סוף סוף זה לא יהיה סימטרי; המערכת תקרוס אל {% equation %}\left|0\right\rangle {% endequation %} בהסתברות {% equation %}\cos^{2}\frac{\pi}{8}{% endequation %} ואל {% equation %}\left|1\right\rangle {% endequation %} בהסתברות {% equation %}\sin^{2}\frac{\pi}{8}{% endequation %}. מבין שתי ההסתברויות, זו של {% equation %}\cos^{2}\frac{\pi}{8}{% endequation %} גדולה משמעותית יותר כי {% equation %}\frac{\pi}{8}{% endequation %} קטן יחסית - לכן בחרנו את הזווית הזו דווקא.

בדומה, אם בהסתברות {% equation %}\frac{1}{2}{% endequation %} אליס תקבל דווקא {% equation %}\left|1\right\rangle {% endequation %} ולא {% equation %}\left|0\right\rangle {% endequation %} המערכת תקרוס למצב {% equation %}\sin\frac{\pi}{8}\left|10\right\rangle +\cos\frac{\pi}{8}\left|11\right\rangle {% endequation %} שנראה לבוב כמו {% equation %}\sin\frac{\pi}{8}\left|0\right\rangle +\cos\frac{\pi}{8}\left|1\right\rangle {% endequation %} והפעם ההסתברות למדוד {% equation %}\left|1\right\rangle {% endequation %} דווקא תהיה {% equation %}\cos^{2}\frac{\pi}{8}{% endequation %}. מה שראינו הוא שלא משנה מה אליס מקבלת, ההסתברות שבוב יקבל את אותו הדבר כמוה היא גדולה יחסית - {% equation %}\cos^{2}\frac{\pi}{8}\ge0.85{% endequation %}.

עכשיו הפאנץ' מגיע: כאשר אליס ובוב מקבלים שניהם 1, ומפעילים שניהם את הטרנספורמציות שלהם, זה הולך "לשבור" את הקורלציה בין שני הקיוביטים שלהם - או ליתר דיוק, להפוך אותה לאנטי-קורלציה (אנטי-קורלציה מלאה פירושה שכאשר אחד הקיוביטים הוא 0 השני הוא 1; שימו לב להבדל המשמעותי בין זה ובין "אין קורלציה". הדבר דומה להיפסטר שמקפיד תמיד לעשות ההפך מהמיינסטרים, ולכן נקבע על ידו).

מכיוון שגם אליס וגם בוב מפעילים טרנספורמציות לינאריות, אולי הכי פשוט לראות מה קורה על ידי היעזרות בכפל מטריצות. המטריצה שמתארת את הפעולה של אליס היא זו:

{% equation %}\left[\begin{array}{cccc}\cos\frac{\pi}{8} & -\sin\frac{\pi}{8} & 0 & 0\\\sin\frac{\pi}{8} & \cos\frac{\pi}{8} & 0 & 0\\0 & 0 & \cos\frac{\pi}{8} & -\sin\frac{\pi}{8}\\0 & 0 & \sin\frac{\pi}{8} & \cos\frac{\pi}{8}\end{array}\right]{% endequation %}

והמטריצה של בוב היא (בדקו!)

{% equation %}\left[\begin{array}{cccc}\cos\frac{\pi}{8} & 0 & \sin\frac{\pi}{8} & 0\\0 & \cos\frac{\pi}{8} & & \sin\frac{\pi}{8}\\-\sin\frac{\pi}{8} & 0 & \cos\frac{\pi}{8} & 0\\0 & -\sin\frac{\pi}{8} & 0 & \cos\frac{\pi}{8}\end{array}\right]{% endequation %}

כפל מטריצות הוא לא כל כך נורא - אפילו אני יכול לחשב אותו. מקבלים:

{% equation %}\left[\begin{array}{cccc}\cos\frac{\pi}{8} & -\sin\frac{\pi}{8} & 0 & 0\\\sin\frac{\pi}{8} & \cos\frac{\pi}{8} & 0 & 0\\0 & 0 & \cos\frac{\pi}{8} & -\sin\frac{\pi}{8}\\0 & 0 & \sin\frac{\pi}{8} & \cos\frac{\pi}{8}\end{array}\right]\left[\begin{array}{cccc}\cos\frac{\pi}{8} & 0 & \sin\frac{\pi}{8} & 0\\0 & \cos\frac{\pi}{8} & & \sin\frac{\pi}{8}\\-\sin\frac{\pi}{8} & 0 & \cos\frac{\pi}{8} & 0\\0 & -\sin\frac{\pi}{8} & 0 & \cos\frac{\pi}{8}\end{array}\right]=\left[\begin{array}{cccc}\cos^{2}\frac{\pi}{8} & \cdots & \cdots & -\sin^{2}\frac{\pi}{8}\\\frac{1}{2}\sin\frac{\pi}{4} & & & \frac{1}{2}\sin\frac{\pi}{4}\\-\frac{1}{2}\sin\frac{\pi}{4} & & & -\frac{1}{2}\sin\frac{\pi}{4}\\-\sin^{2}\frac{\pi}{8} & \cdots & \cdots & \cos^{2}\frac{\pi}{8}\end{array}\right]{% endequation %}

לא טרחתי לחשב את העמודות במרכז כי כשנכפול את המטריצה במצב הקוונטי {% equation %}\left|00\right\rangle +\left|11\right\rangle {% endequation %} העמודות הללו לא ישפיעו. אחרי הכפל נקבל את המצב הבא:

{% equation %}\left(\cos^{2}\frac{\pi}{8}-\sin^{2}\frac{\pi}{8}\right)\left|00\right\rangle +\sin\frac{\pi}{4}\left|01\right\rangle -\sin\frac{\pi}{4}\left|10\right\rangle +\left(\cos^{2}\frac{\pi}{8}-\sin^{2}\frac{\pi}{8}\right)\left|11\right\rangle {% endequation %}

השתמשתי קודם בכך ש-{% equation %}\cos\theta\sin\theta=\frac{1}{2}\sin2\theta{% endequation %} - זהות הזווית הכפולה עבור סינוס. עבור קוסינוס יש זהות דומה: {% equation %}\cos2\theta=\cos^{2}\theta-\sin^{2}\theta{% endequation %}. לכן המצב הקוונטי שהגענו אליו הוא

{% equation %}\cos\frac{\pi}{4}\left|00\right\rangle +\sin\frac{\pi}{4}\left|01\right\rangle -\sin\frac{\pi}{4}\left|10\right\rangle +\cos\frac{\pi}{4}\left|11\right\rangle {% endequation %}

ועכשיו אולי ברור למה בחרנו את הזווית {% equation %}\theta=\frac{\pi}{8}{% endequation %}; זה מכיוון ש-{% equation %}\frac{\pi}{4}{% endequation %} מקיימת ש-{% equation %}\sin\frac{\pi}{4}=\cos\frac{\pi}{4}{% endequation %}, מה שאומר שכל המקדמים במצב שקיבלנו הם זהים בערכם המוחלט - ואתם כבר מבינים שזה אומר שהמדידה המשותפת של אליס-ואז-בוב תיתן כל זוג תוצאות באותה הסתברות בדיוק - כלומר, אם גם אליס וגם בוב ביצעו טרנספורמציה על המערכת, הם "שברו" לגמרי את הקורלציה בין הקיוביטים (ולא סתם הפכו אותה לאנטי-קורלציה). עכשיו, מכיוון ש-{% equation %}x=y=1{% endequation %} אליס ובוב צריכים להחזיר תוצאה שונה - מה שיקרה אם הם ימדדו את {% equation %}\left|10\right\rangle {% endequation %} או {% equation %}\left|01\right\rangle {% endequation %}, בהסתברות {% equation %}\frac{1}{2}{% endequation %}.

עכשיו אפשר לנתח את האסטרטגיה הזו של אליס ובוב ומה ההסתברות שלהם לנצח במשחק. אמרנו שמנהל המשחק מגריל את {% equation %}x,y{% endequation %} באקראי, כך שאנחנו מפרידים בין שלושה מקרים:
<ol>
	<li>{% equation %}x=y=0{% endequation %} בהסתברות {% equation %}\frac{1}{4}{% endequation %} ואז אליס ובוב מנצחים בהסתברות 1.</li>
	<li>{% equation %}x=y=1{% endequation %} בהסתברות {% equation %}\frac{1}{4}{% endequation %} ואז אליס ובוב מנצחים בהסתברות {% equation %}\frac{1}{2}{% endequation %}.</li>
	<li>{% equation %}x\ne y{% endequation %} בהסתברות {% equation %}\frac{1}{2}{% endequation %} ואז אליס ובוב מנצחים בהסתברות שגדולה מ-{% equation %}0.85{% endequation %}.</li>
</ol>
סך הכל הסתברות ההצלחה של אליס ובוב היא לפחות {% equation %}\frac{1}{4}\cdot1+\frac{1}{4}\cdot\frac{1}{2}+\frac{1}{2}\cdot\frac{17}{20}=\frac{1}{2}\frac{10+5+17}{20}=\frac{32}{40}=\frac{4}{5}=0.8{% endequation %} - וזו הסתברות גדולה מ-{% equation %}0.75{% endequation %}!

אז מה יש לנו כאן? מצד אחד, ההפרש בין {% equation %}0.8{% endequation %} ל-{% equation %}0.75{% endequation %} הוא לא דרמטי במיוחד, והמשחק כולו נראה אבסורדי לגמרי ולא שימושי בעליל, ולכן התוצאה לא נראית חשובה במיוחד מבחינה פרקטית; אבל המשמעות שלה מבחינה תיאורטית היא לא זניחה בכלל - היא ממחישה מה חישובים קוונטים נותנים לנו שחישוב רגיל לא יכול לתת. מצד שני, לקרוא לזה "חישוב קוונטי" זו קצת רמאות - הפואנטה כאן היא לא החישוב; היא ה<strong>תקשורת</strong> שתורת הקוונטים מאפשרת לאליס ובוב לבצע - היא מאפשרת להם לעשות סוג מוגבל של קורלציית מידע גם כשהם מרוחקים, וכאן הקסם של הסופרפוזיציה לא תורם אלא מפריע (כי במקום שאליס פשוט תשלח ביט באופן קסום אל בוב הם עושים טרנספורמציות למצבים קוונטיים ומודדים אותם ומקווים שיהיה מזל עם המדידות). לכן זו דוגמה טובה להמחשת ה<strong>אתגר</strong> שיש בחישוב קוונטי עם התמודדות עם <strong>מגבלות</strong> על החישוב.

אבל רגע, אתם אומרים, תורת הקוונטים מאפשרת לאליס ובוב לתקשר יותר מהר ממהירות האור, וזה סותר את תורת היחסות הפרטית! ובכן, כן, זה ההקשר שבו המצב הקוונטי {% equation %}\left|00\right\rangle +\left|11\right\rangle {% endequation %} הופיע מלכתחילה, אבל כמובן שהסיפור לא עד כדי כך פשוט והסתירה לא כל כך ברורה. אדבר על כך בפוסט הבא.

