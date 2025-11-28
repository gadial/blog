---
id: 3565
title: "כמה חלוקות יש, ואיך זה קשור לאוילר ולמספרים מחומשים?"
date: 2018-03-11 08:07:32
layout: post
categories: 
  - קומבינטוריקה
tags: 
  - משפט המספרים המחומשים
  - פונקציות יוצרות
  - פונקציית החלוקה
---
<h2>פרק ראשון, ובו מככבים בעיה קומבינטורית מסתורית, פתרון מסתורי עוד יותר ונוסחאות מסתוריות יותר מדי</h2>
אני רוצה לדבר הפעם על מה שלטעמי היא הבעיה היפה והמעניינת ביותר בקומבינטוריקה בסיסית - בעיית הספירה של <strong>חלוקות</strong> של מספרים טבעיים. מה זו חלוקה של מספר {% equation %}n{% endequation %}? זו דרך לכתוב את {% equation %}n{% endequation %} כסכום של מספרים טבעיים חיוביים, כשאין חשיבות לסדר של המחוברים. למשל, {% equation %}3=1+2{% endequation %} היא חלוקה של {% equation %}3{% endequation %}, והיא זהה ל-{% equation %}2+1{% endequation %}. עוד חלוקות אפשריות של 3 הן פשוט 3 עצמה, ו-{% equation %}1+1+1{% endequation %}. אם כן, ל-3 יש {% equation %}3{% endequation %} חלוקות. קל לראות של-1 יש חלוקה אחת, ול-2 יש שתי חלוקות. האם ל-4 יהיו, אם כן, 4 חלוקות? ובכן, לא, יש 5:
<ol>
 	<li>4</li>
 	<li>{% equation %}1+3{% endequation %}</li>
 	<li>{% equation %}2+2{% endequation %}</li>
 	<li>{% equation %}1+1+2{% endequation %}</li>
 	<li>{% equation %}1+1+1+1{% endequation %}</li>
</ol>
אפשר להגדיר כך פונקציה: {% equation %}p\left(n\right){% endequation %} היא מספר החלוקות של המספר הטבעי {% equation %}n{% endequation %} (ל-0 יש חלוקה יחידה, "ריקה"). הסדרה {% equation %}p\left(0\right),p\left(1\right),p\left(2\right),\dots{% endequation %} מתחילה כך:

{% equation %}1,1,2,3,5,7,11,15,22,30,42,56,77,\dots{% endequation %}

ונשאלת השאלה - האם יש דרך חישוב פשוטה עבור {% equation %}p\left(n\right){% endequation %}?

כדי לראות מה זו "דרך חישוב פשוטה", בואו נסתכל לרגע על בעיה דומה: יש לנו {% equation %}n{% endequation %} כדורים שנמצאים ב-{% equation %}k{% endequation %} תאים הממוספרים ב-{% equation %}1,2,\dots,k{% endequation %}, (כשאפשר תאים ריקים ואפשר יותר מכדור אחד בתא). כמה סיטואציות אפשריות כאלו יש? ובכן, זה מה שנקרא בקומבינטוריקה <strong>בחירה עם החזרה וללא חשיבות לסדר</strong>: בחירה - לכל כדור בוחרים תא; עם החזרה - אפשר לבחור את אותו תא יותר מפעם אחת; ללא חשיבות לסדר - מה שמתעניינים בו הוא רק כמה כדורים יש בכל תא בסוף התהליך, לא כמה תהליכי חלוקה קיימים. <a href="http://gadial.net/2010/07/08/combinatorics_choices/">יש לי פוסט</a> שבו אני פותר את הבעיה הזו, והפתרון (שלא חשוב לפוסט הזה) הוא מה שמסומן ב-{% equation %}{n+k-1 \choose k}{% endequation %} והוא סימון מקוצר ל-{% equation %}\frac{\left(n+k-1\right)!}{k!\left(n-1\right)!}{% endequation %}. זו נוסחה סגורה פשוטה שאפשר לחשב ממנה ערכים מספריים בקלות רבה יחסית.

אם ננסה לעשות ניתוח דומה עבור פונקציית החלוקה, מהר מאוד ניתקל בקשיים ונראה שהבעיה הזו חמקמקה הרבה משנראה במבט ראשון. עיקר הקושי הוא שקל לבצע בטעות <strong>ספירה כפולה</strong> כשמנסים לעשות הפרדה למקרים. הנה דוגמא עבור ניתוח שגוי של מספר החלוקות של 4: אני אומר, בואו ניקח מספר {% equation %}1\le n\le4{% endequation %}, ניקח את {% equation %}4-n{% endequation %} ונחשב את <strong>כל</strong> החלוקות שלו, נוסיף לכל אחת מהן את {% equation %}n{% endequation %} והופס - קיבלנו חלוקה של 4 ואפשר להוסיף אותה לספירה. כל מה שנשאר לעשות הוא לעבור על כל הערכים האפשריים של {% equation %}n{% endequation %}.

במילים אחרות, אני מציע לבצע את החישוב הבא: {% equation %}p\left(4\right)=p\left(3\right)+p\left(2\right)+p\left(1\right)+p\left(0\right)=3+2+1+1=7{% endequation %}. קיבלתי תוצאה גדולה מדי - ספרתי שתי חלוקות פעמיים. את מי? ובכן, אם {% equation %}n=2{% endequation %} אז אני בונה את החלוקה {% equation %}2+\left(1+1\right){% endequation %} (החלק בסוגריים הוא חלוקה של {% equation %}2=4-n{% endequation %} במקרה הזה). אם לעומת זאת {% equation %}n=1{% endequation %} אז אני בונה את החלוקה {% equation %}1+\left(2+1\right){% endequation %} (כאן הסוגריים הם חלוקה של {% equation %}3=4-n{% endequation %}). שתי החלוקות הללו הן <strong>אותו דבר</strong>. הסדר של האיברים בסכום שונה, אבל אמרנו שזה לא משנה לנו, ומכאן הספירה הכפולה.

אם השיטה שלי הייתה עובדת והיינו מקבלים ש-{% equation %}p\left(n\right){% endequation %} שווה לסכום כל ה-{% equation %}p\left(k\right){% endequation %}-ים עבור {% equation %}k&lt;n{% endequation %}, האם הייתם מסכימים שזו דרך חישוב פשוטה? מצד אחד, זה אומר שכדי לחשב את {% equation %}p\left(n\right){% endequation %} צריך לחשב את <strong>כל</strong> האיברים שלפניו בסדרה; מצד שני, החישוב עצמו הוא מאוד פשוט. חשבו לרגע על סדרת פיבונאצ'י שמוגדרת באמצעות הכלל {% equation %}F\left(0\right)=0,F\left(1\right)=1{% endequation %} ו-{% equation %}F\left(n\right)=F\left(n-1\right)+F\left(n-2\right){% endequation %} לכל {% equation %}n\ge2{% endequation %}; גם בשביל לחשב את {% equation %}F\left(100\right){% endequation %} צריך לחשב קודם כל את כל האיברים הקודמים, ועדיין החישוב הוא פשוט יחסית (יש גם נוסחה סגורה לפיבונאצ'י, אבל זה לא אומר שיותר קל להשתמש בה בחישובים).

ובכן, מה אם אספר לכם ש<strong>אפשר</strong> לחשב את פונקציית החלוקה באופן רקורסיבי שכזה, אבל במקום לחבר את <strong>כל</strong> ה-{% equation %}p\left(k\right){% endequation %}-ים עבור {% equation %}k&lt;n{% endequation %}, צריך לחבר (או לחסר) רק <strong>חלק מהם</strong>? למשל, {% equation %}p\left(4\right)=p\left(3\right)+p\left(2\right){% endequation %}; ואם תבדקו בעזרת הרשימה שנתתי לעיל תוכלו גם לראות ש-

{% equation %}p\left(5\right)=p\left(4\right)+p\left(3\right)-p\left(0\right){% endequation %}

{% equation %}p\left(6\right)=p\left(5\right)+p\left(4\right)-p\left(1\right){% endequation %}

וכך זה נמשך אבל הולך ומסתבך מבחינת "את מי לחבר/לחסר". למשל:

{% equation %}p\left(17\right)=p\left(16\right)+p\left(15\right)-p\left(12\right)-p\left(10\right)+p\left(5\right){% endequation %}

מה החוקיות הכללית פה? כאן נכנס לתמונה מי שנקראים <strong>מספרים מחומשים</strong>. מספר מחומש {% equation %}t\left(k\right){% endequation %} הוא מספר מהצורה {% equation %}t\left(k\right)=\frac{k\left(3k-1\right)}{2}{% endequation %} עבור {% equation %}k{% endequation %} שלם ששונה מאפס - חיובי או שלילי (האות {% equation %}t{% endequation %} היא לא סימון סטנדרטי; אני משתמש בה כי הסימון הסטנדרטי משתמש ב-{% equation %}p{% endequation %} שכבר תפוס לתיאור חלוקות). הרעיון הוא שכדי לחשב את {% equation %}p\left(n\right){% endequation %} סוכמים את כל האיברים מהצורה {% equation %}p\left(n-t\right){% endequation %} כאשר {% equation %}t{% endequation %} הוא מספר מחומש שקטן מ-{% equation %}n{% endequation %}; השאלה האם לחבר או לחסר את {% equation %}p\left(n-t\right){% endequation %} תלויה בזוגיות של ה-{% equation %}k{% endequation %} שהניב אותו: אם הוא אי-זוגי, אז מחברים, ואם הוא זוגי אז מחסרים. אם נשב לכתוב את סדרת המספרים המחומשים נראה שהיא שווה ל

{% equation %}1,2,5,7,12,15,22,26,\dots{% endequation %}

ולכן הנוסחה הכללית לחישוב מספר החלוקות היא

{% equation %}p\left(n\right)=p\left(n-1\right)+p\left(n-2\right)-p\left(n-5\right)-p\left(n-7\right)+p\left(n-12\right)+p\left(n-15\right)-p\left(n-22\right)-p\left(n-26\right)+\dots{% endequation %}

וכן הלאה וכן הלאה. זו תוצאה מרהיבה ממש לטעמי (בפרט קל להעריך אותה אם מנסים לחשב מספרית את {% equation %}p\left(n\right){% endequation %} בדרכים אחרות ורואים עד כמה זה מעיק), אבל היא נראית גם הזויה לחלוטין - מה המשמעות הקומבינטורית של נוסחת הנסיגה הזו? למה מחברים או <strong>מחסרים</strong>? למה דווקא המספרים ה"מחומשים" הללו? ובכן, הפוסט הזה ינסה לענות על השאלות הללו ברמה כלשהי, אם כי אני מזהיר מראש שאין לי אינטואיציה קומבינטורית לגבי "למה הנוסחה עובדת"; אני הולך להוכיח אותה בעזרת כלי קומבינטורי חזק מאוד שנקרא <strong>פונקציות יוצרות</strong>. הכלי הזה נותן לי תחושה חזקה מאוד של "למה זה נכון", ועם זאת לא נותן לי שום רמז לגבי משמעות קומבינטורית אפשרית של נוסחת הנסיגה. זה פחות מפריע לי כי אני חושב שהבעיה הספציפית הזו של חלוקות היא הזדמנות מושלמת להראות מה הן פונקציות יוצרות ומה הכוח שלהן.

את הסיפור של פונקציית החלוקה שאני רוצה לספר אפשר לתמצת לשתי משוואות שבמבט ראשון יכולות להיראות חסרות פשר, אפילו שגויות, וננסה להבין אותן כאן:
<ul>
 	<li>{% equation %}\sum_{n=0}^{\infty}p\left(n\right)x^{n}=\prod_{n=1}^{\infty}\frac{1}{\left(1-x^{n}\right)}{% endequation %}</li>
 	<li>{% equation %}\prod_{n=1}^{\infty}\left(1-x^{n}\right)=\sum_{k=-\infty}^{\infty}\left(-1\right)^{k+1}x^{t\left(k\right)}{% endequation %}</li>
</ul>
הנוסחה הראשונה עוסקת בפונקציה היוצרת של הפונקציה {% equation %}p{% endequation %} של מספר החלוקות, והשניה איכשהו מכניסה פנימה את הפונקציה {% equation %}t\left(k\right){% endequation %} של המספרים המחומשים. הקישור של שתיהן יחד נותן לנו את נוסחת הנסיגה שראינו קודם. אנחנו נרצה לעשות שלושה דברים:
<ol>
 	<li>להבין למה הנוסחה הראשונה נכונה - זה יהיה קל יחסית, אחרי שנבין מהן פונקציות יוצרות.</li>
 	<li>להבין למה הנוסחה השניה נכונה - אני הולך להראות הוכחה קומבינטורית מקסימה לדבר הזה.</li>
 	<li>להבין איך הקשר בין שתי הנוסחאות נותן לנו את נוסחת הנסיגה.</li>
</ol>
הנוסחאות הללו התגלו לראשונה ככל הנראה בידי לאונרד אוילר, בשנת 1741. האזכור הכתוב הראשון שיש לנו להן הוא במכתב מאותה שנה ששלח דניאל ברנולי לאוילר ומתייחס אליהן, ככל הנראה בתגובה למכתב של אוילר (שלא נמצא) שתיאר אותן. אוילר הציג באותה שנה מאמר שמתאר את הנוסחאות הללו ושימושיהן, אבל ההוכחה שאני הולך להראות לנוסחה השניה היא מ-1881, של מתמטיקאי אמריקאי בשם פרנקלין שלא הצלחתי למצוא עליו שום מידע. אפשר להבין את ההוכחה של פרנקלין גם בלי להבין מה הולך עם הפורמליסטיקה של הנוסחאות, והיא מאוד יפה לכשעצמה, כך שאציג אותה בפוסט נפרד; גם אם הלכתם לאיבוד פה אתם יכולים לדלג אל הפוסט הבא בשבילה.
<h2>פרק שני, ובו בהחלט לא נעסוק בחדו"א בשום צורה</h2>
בואו נתחיל עם להבין מה בכלל המשמעות של הנוסחאות של אוילר. נסתכל באגף שמאל של הנוסחה הראשונה:

{% equation %}\sum_{n=0}^{\infty}p\left(n\right)x^{n}=\prod_{n=1}^{\infty}\frac{1}{\left(1-x^{n}\right)}{% endequation %}

מה זה {% equation %}\sum_{n=0}^{\infty}p\left(n\right)x^{n}{% endequation %}? יש כאן <strong>סכום אינסופי</strong>, יצור שאנחנו רגילים אליו מחדו"א. בחדו"א מדברים על <strong>טורי מספרים</strong>, למשל הטור {% equation %}\sum_{n=1}^{\infty}\frac{1}{2^{n}}{% endequation %}. יש הגדרות מקובלות שמתבססות על מושג <strong>הגבול</strong> שאומרות מתי סביר להתאים ערך של "סכום" לטור כזה ומתי לא - בהגדרות הללו יוצא, למשל, ש-{% equation %}\sum_{n=1}^{\infty}\frac{1}{2^{n}}=1{% endequation %}. מכירים את זה? מצויין. אז אני מבקש מכם <strong>לשכוח את זה לגמרי</strong> בפוסט הזה. לא נדבר על מושג הגבול ולא נזדקק לו ולא נזדקק לחדו"א. לא על זה מדובר פה.

טוב, אני משקר. זה <strong>קצת</strong> קשור למה שמדובר עליו פה. <strong>אפשר</strong> להכניס חדו"א לתמונה כשמתעסקים עם פונקציות יוצרות, אבל למטרות ניתוחים שלא יהיו רלוונטיים לנו כאן כלל. בנוסף, אין ספק שעבור אוילר, החדו"א הייתה ההצדקה לכך שאפשר להשתמש בכלל בנוסחאות הללו. אוילר חי בתקופה שבה החדו"א בפרט והמתמטיקה בכלל לא פורמלו עד הסוף, ומושג הגבול בכלל לא הומצא, ומתמטיקאים עשו מניפולציות של ביטויים כמו זה שלעיל באופן די חופשי, כשהם מסתמכים על האינטואיציה שלהם ועל זה שדברים עובדים בסוף. שלא יהיה ספק, כשעשה את זה מתמטיקאי פנטסטי כמו אוילר, זה באמת עבד; הנה <a href="http://gadial.net/2009/05/17/euler_proof_infinity_of_primes/">עוד דוגמא</a> נאה לזה, שמערבת את פונקציית הזטא של רימן. עם זאת, אני באמת הולך להתעלם מכל זה ולהציג את הנושא בגישה הפורמליסטית והמודרנית יותר, שאני מקווה שתרגיע גם את הסקפטיים ביותר מביניכם שמרגישים שמשהו לא מוגדר פה טוב בכלל.

בואו ניתן עוד מבט בסכום:

{% equation %}\sum_{n=0}^{\infty}p\left(n\right)x^{n}{% endequation %}

כאן סוכמים לא רק מספרים, אלא גם חזקות של ה<strong>משתנה</strong> {% equation %}x{% endequation %}. זה מזכיר את המושג של <strong>טור חזקות</strong> מחדו"א, ואני אכן קורא ליצור הזה <strong>טור חזקות פורמלי</strong>, אלא שאני שוב רוצה להסתייג - הרעיון בטורי חזקות הוא שאפשר להציב ערכים שונים ומשונים בתוך {% equation %}x{% endequation %}, לקבל טור מספרים רגיל ואז לראות האם הוא מתכנס, ואל מה. אני לא הולך לעשות את זה - בשום מקום בהמשך לא נציב משהו בתוך {% equation %}x{% endequation %}. אז רגע - אם לא מציבים כלום בתוך {% equation %}x{% endequation %}, בשביל מה הוא כאן? האם זה סתם סימון? דרך מסובכת לכתוב את הסדרה {% equation %}\left(p\left(0\right),p\left(1\right),p\left(2\right),\dots\right){% endequation %}? ובכן, זו אכן רק דרך לכתוב את הסדרה הזו, אבל אני טוען שלא דרך מסובכת אלא ההפך - דרך יותר <strong>פשוטה</strong>.

בואו ניזכר לרגע בפולינומים. את הפולינום {% equation %}x^{3}+2x^{2}+4{% endequation %} אפשר גם לכתוב בתור סדרה: {% equation %}\left(4,0,2,1\right){% endequation %}. אפשר לראות שאם אחד המקדמים הוא 0, אז הפולינום "חסכוני" יותר בכך שלא חייבים לכתוב את האיבר שמתאים לו, אבל זה לא כזה קריטי. החלק המעניין מתחיל אם אני רוצה לכפול את הפולינום הזה בפולינום אחר. למשל:

{% equation %}\left(x^{3}+2x^{2}+4\right)\left(x^{2}+1\right)=\left(x^{5}+2x^{4}+4x^{2}\right)+\left(x^{3}+2x^{2}+4\right)={% endequation %}

{% equation %}=x^{5}+2x^{4}+x^{3}+6x^{2}+4{% endequation %}

כאן הכפל קל יחסית כשפותחים סוגריים ומשתמשים בכלל החזקות {% equation %}x^{a}\cdot x^{b}=x^{a+b}{% endequation %}, שהוא מבחינתנו כאן הגדרה ולא משהו שיש להוכיח. בואו נסתכל עכשיו איך זה נראה בתור "כפל סדרות":

{% equation %}\left(4,0,2,1\right)\times\left(1,0,1\right)=\left(4,0,6,1,2,5\right){% endequation %}

לא לגמרי ברור פה איך אגף ימין התקבל מאגף שמאל. הכלל שעל פיו החישוב מתבצע נקרא <strong>קונבולוציה</strong>, וזה הולך כך: אם {% equation %}\left(a_{1},a_{2},\dots,a_{n}\right){% endequation %} ו-{% equation %}\left(b_{1},\dots,b_{m}\right){% endequation %} הן סדרות אז נגדיר את הקונבולוציה שלהן

{% equation %}\left(a_{1},\dots,a_{n}\right)*\left(b_{1},\dots,b_{m}\right)=\left(c_{1},\dots,c_{n+m}\right){% endequation %}

על ידי הכלל {% equation %}c_{k}=\sum_{i=1}^{k}a_{i}b_{m-i}{% endequation %} (תוך המוסכמה ש-{% equation %}b_{i}=0{% endequation %} עבור {% equation %}i\le0{% endequation %}). נראה מבלבל? בהחלט, אבל זו בסך הכל דרך "נטולת {% equation %}x{% endequation %}" לתאר את פעולת הכפל הרגילה של פולינומים. כך שהייצוג ה"מיותר" של הפולינום הוא דווקא מועיל בכך שהוא נותן לנו אינטואיציה יותר טובה לפעולת הכפל.

עכשיו בואו נדבר על כפל של שני טורים <strong>אינסופיים</strong>, {% equation %}\sum_{n=0}^{\infty}a\left(n\right)x^{n}{% endequation %} ו-{% equation %}\sum_{n=0}^{\infty}b\left(n\right)x^{n}{% endequation %}. על פניו אפשר לחשוש שאם הטורים לא "מתכנסים" אז אסור להכפיל אותם או משהו דומה לכך, אבל אם שמים את זה בצד ופשוט כופלים אותם כמו כפל פולינומים רגיל, מגלים שהתוצאה היא טור {% equation %}\sum_{n=0}^{\infty}c\left(n\right)x^{n}{% endequation %} שכל איבר בו מוגדר על ידי המשוואה

{% equation %}c\left(n\right)=\sum_{k=0}^{n}a\left(k\right)b\left(n-k\right){% endequation %}

(שוב, תחת המוסכמה ש-{% equation %}b\left(t\right)=0{% endequation %} אם {% equation %}t&lt;0{% endequation %}).

כלומר, כדי לחשב את <strong>המקדמים</strong> בטור החזקות של המכפלה אנחנו צריכים, לכל מקדם, לחשב סכום <strong>סופי</strong> של מספרים. סכום סופי שכזה תמיד קיים, כך שהמכפלה של שני טורי חזקות היא מוגדרת היטב גם בלי להיכנס לשאלות של התכנסות. זה עונה לשאלה האם <strong>אפשר</strong> לעבוד ככה עם טורי חזקות פורמליים. נשאר רק לענות לשאלה למה <strong>כדאי</strong> לעשות את זה.

כדי לתרגל לרגע את הכפל, בואו נסתכל על טור החזקות הפורמלי {% equation %}\sum_{n=0}^{\infty}a\left(n\right)x^{n}{% endequation %} שבו {% equation %}a\left(n\right)=1{% endequation %} לכל {% equation %}n{% endequation %}, ועל הטור {% equation %}\sum_{n=0}^{\infty}b\left(n\right)x^{n}{% endequation %} שבו {% equation %}b\left(0\right)=1{% endequation %} ו-{% equation %}b\left(1\right)=-1{% endequation %} ו-{% equation %}b\left(n\right)=0{% endequation %} לכל {% equation %}n&gt;1{% endequation %}. אפשר לכתוב אותם בצורה מקוצרת כך: {% equation %}\left(1+x+x^{2}+\dots\right){% endequation %} לטור הראשון ו-{% equation %}1-x{% endequation %} לטור השני. אם נכפול את שניהם, קל לראות שנקבל לכל {% equation %}n&gt;0{% endequation %} את האיבר הכללי:

{% equation %}c\left(n\right)=\sum_{k=0}^{n}a\left(k\right)b\left(n-k\right)=a\left(n-1\right)b\left(1\right)+a\left(n\right)b\left(0\right)=-1+1=0{% endequation %}

ואילו עבור {% equation %}n=0{% endequation %} נקבל איבר כללי {% equation %}c\left(n\right)=1{% endequation %}. אפשר לכתוב את זה כך:

{% equation %}\left(1+x+x^{2}+\dots\right)\left(1-x\right)=1{% endequation %}

וזה מוביל לעוד מוסכמת כתיבה שאני מבקש שתהיו סלחניים אליה:

{% equation %}\left(1+x+x^{2}+\dots\right)=\frac{1}{1-x}{% endequation %}

אתם אולי מכירים את השוויון הזה בתור "סכום טור הנדסי אינסופי מתכנס", אבל <strong>שוב</strong> אני רוצה להזהיר שאני לא מדבר פה על התכנסויות במובן של חדו"א! אגף ימין כאן הוא סימון מקוצר; זו דרך להגיד "טור החזקות הפורמלי שכאשר כופלים אותו ב-{% equation %}\left(1-x\right){% endequation %} מקבלים 1". באופן כללי אם

{% equation %}\sum a\left(n\right)x^{n}\cdot\sum b\left(n\right)x^{n}=\sum c\left(n\right)x^{n}{% endequation %}

אפשר יהיה לכתוב את זה גם בתור

{% equation %}\sum a\left(n\right)x^{n}=\frac{\sum c\left(n\right)x^{n}}{\sum b\left(n\right)x^{n}}{% endequation %}

ועוד נראה כמה שיטת הייצוג הזו מועילה לנו בהמשך. לבינתיים, בואו נכליל את ה"טור הנדסי" שראינו קודם - קל לבדוק בדיוק באותה שיטה שמתקיים גם

{% equation %}\left(1+x^{n}+x^{2n}+x^{3n}+\dots\right)=\frac{1}{1-x^{n}}{% endequation %}

לכל {% equation %}n{% endequation %} טבעי. למשל

{% equation %}\left(1+x^{2}+x^{4}+\dots\right)=\frac{1}{1-x^{2}}{% endequation %}

{% equation %}\left(1+x^{3}+x^{6}+\dots\right)=\frac{1}{1-x^{3}}{% endequation %}

אפשר עכשיו <strong>לכפול</strong> את שתי המשוואות, ונקבל:

{% equation %}\left(1+x^{2}+\dots\right)\left(1+x^{3}+\dots\right)=\frac{1}{\left(1-x^{2}\right)}\cdot\frac{1}{\left(1-x^{3}\right)}{% endequation %}

כמובן, צריך לבדוק שזה אכן עובד, פורמלית, אבל זה עובד. ואם זה עובד לשני מוכפלים, זה יעבוד לכל מספר סופי של מוכפלים, אבל אנחנו נהיה שאפתנים אפילו יותר ונעשה את זה עבור <strong>אינסוף</strong> מוכפלים! אבל לפני זה, בואו ננסה להבין מה בעצם המשמעות הקומבינטורית של הכפלה כזו, כי זה בדיוק מה שיתן לנו את השוויון {% equation %}\sum_{n=0}^{\infty}p\left(n\right)x^{n}=\prod_{n=1}^{\infty}\frac{1}{\left(1-x^{n}\right)}{% endequation %} שאנחנו חותרים אליו.

בדוגמה שלנו, אם נפתח את הסוגריים של המכפלה נקבל את המחוברים הבאים: {% equation %}1\cdot1+x^{2}\cdot1+1\cdot x^{3}+x^{2}\cdot x^{3}+x^{4}\cdot1+\dots{% endequation %}. זה בסך הכל שווה ל-{% equation %}1+x^{2}+x^{3}+x^{4}+x^{5}+2x^{6}+\dots{% endequation %} - רגע רגע רגע, מאיפה הגיע המקדם 2 ל-{% equation %}x^{6}{% endequation %}? ובכן, כי הוא נוצר בעזרת שני מוכפלים כי הוא מופיע בשני זוגות הסוגריים. אפילו יותר מעניין יהיה {% equation %}x^{12}{% endequation %} שיכול להיווצר בדרכים הבאות: {% equation %}x^{12}\cdot1,1\cdot x^{12},x^{6}\cdot x^{6}{% endequation %}, ולכן המקדם שלו יהיה 3, וכן הלאה. אנחנו רואים שהמקדם של {% equation %}x^{n}{% endequation %} סופר את <strong>הדרכים השונות</strong> שבהן ניתן לכתוב את {% equation %}n{% endequation %} בתור סכום מהצורה {% equation %}n=2a+3b{% endequation %}. כל דרך שכזו נותנת לנו איבר מפורש, {% equation %}x^{2a}\cdot x^{3b}=x^{n}{% endequation %} שיתווסף לסכום.

הנה הפרשנות הקומבינטורית של הסיפור הזה. נניח שיש בעולם שלנו אובייקטים מגדלים שונים ומשונים שהם מספר טבעי, וש-{% equation %}\sum a\left(n\right)x^{n}{% endequation %} סופר חלק מהם - בדיוק {% equation %}a\left(n\right){% endequation %} אובייקטים מ"גודל" {% equation %}n{% endequation %}. באופן דומה {% equation %}\sum b\left(n\right)x^{n}{% endequation %} סופר קבוצה אחרת של אובייקטים שכאלה. במקרה שלנו האובייקטים הם חלוקות של מספרים טבעיים כשה"גודל" של חלוקה הוא סכום האיברים שלה; {% equation %}\sum x^{2n}{% endequation %} סופר לנו כמה פירוקים לסכום של 2 בלבד יש (או 0 או 1, תלוי אם המספר זוגי) ו-{% equation %}\sum x^{3n}{% endequation %} סופר כמה פירוקים לסכום של 3 בלבד יש (שוב, או 0 או 1, תלוי אם המספר מתחלק ב-3 או לא). למשל {% equation %}x^{6}{% endequation %} במקרה הראשון מציין את הפירוק {% equation %}2+2+2{% endequation %} ובמקרה השני את הפירוק {% equation %}3+3{% endequation %}.

כעת, <strong>מכפלה</strong> של שתי פונקציות יוצרות מתאימה לבניה הקומבינטורית הבאה: לכל זוג אפשרי של אובייקט מסוג ראשון ואובייקט מסוג שני אנחנו בונים אובייקט חדש ש"מורכב מהם" והגודל שלו הוא סכום הגדלים שלהם. אם אין אובייקט שיכול להתקבל משני זוגות שונים, אז הפונקציה היוצרת של המכפלה סופרת בדיוק כמה אובייקטים יכולים להיווצר ככה. כך למשל אצלנו האיבר {% equation %}x^{10}{% endequation %} במכפלה, שאומר "חלוקה אחת של 10" נוצר מזוג החלוקות {% equation %}2+2{% endequation %} ו-{% equation %}3+3{% endequation %}, שמתאימות לאיברים {% equation %}x^{4}{% endequation %} ו-{% equation %}x^{6}{% endequation %} בפונקציות היוצרות הראשונה והשניה. באופן דומה, המקדם של {% equation %}x^{3}{% endequation %} הוא 1, שמציין את האופן שבו אפשר ליצור את {% equation %}3{% endequation %} מהחלוקות "3" ו-"0" (כלומר, מחברים 3 פעם אחת, ומחברים 2 אפס פעמים).

אם נכפול עכשיו <strong>שלוש</strong> פונקציות יוצרות, המשמעות תישאר זהה: איברים שאפשר לבנות על ידי לקיחה של שלשה של אובייקטים והרכבה שלהם ביחד. למשל, את {% equation %}4{% endequation %} אפשר להציג בתור החלוקות הבאות:

{% equation %}4{% endequation %}

{% equation %}2+2{% endequation %}

{% equation %}1+3{% endequation %}

{% equation %}1+1+2{% endequation %}

אז אם אני אפתח את המכפלה

{% equation %}\left(1+x+x^{2}+\dots\right)\left(1+x^{2}+x^{4}+\dots\right)\left(1+x^{3}+x^{6}+\dots\right){% endequation %}

אני אקבל את המקדם {% equation %}3x^{4}{% endequation %}, שמייצג את שלוש החלוקות שבהן משתתפים רק 1,2,3; החלוקה 4 תתקבל רק אם אוסיף למכפלה גם את {% equation %}\left(1+x^{4}+x^{8}+\dots\right){% endequation %}.

עכשיו אוילר אומר שני דברים. ראשית, במקום לכתוב סימון ארוך ומסורבל כמו {% equation %}\left(1+x^{t}+x^{2t}+\dots\right){% endequation %} כל פעם מחדש, בואו נכתוב {% equation %}\frac{1}{\left(1-x^{t}\right)}{% endequation %}; כבר ראינו שזה אותו דבר. שנית, על פי הנימוק שנתנו כאן {% equation %}\prod_{t=1}^{k}\frac{1}{\left(1-x^{t}\right)}{% endequation %} ייתן לנו את הפונקציה היוצרת של מספר הדרכים לחלק כל מספר טבעי לסכום של מספרים מ-1 ועד {% equation %}k{% endequation %}, כלומר את מספר הפתרונות של המשוואה {% equation %}1\cdot x_{1}+2\cdot x_{2}+\dots+k\cdot x_{k}=n{% endequation %}, לכל {% equation %}n{% endequation %} טבעי. יש התאמה חד-חד-ערכית ועל ברורה בין פתרונות כאלו לבין האיברים שמתקבלים מפתיחת המכפלה {% equation %}\prod_{t=1}^{k}\left(1+x^{t}+x^{2t}+\dots\right){% endequation %}: הפתרון {% equation %}x_{1}=a_{1},\dots,x_{k}=a_{k}{% endequation %} מתאים לאיבר

{% equation %}x^{a_{1}\cdot1}\cdot x^{a_{2}\cdot2}\cdots x^{a_{k}\cdot k}=x^{a_{1}\cdot1+\dots+a_{k}\cdot k}=x^{n}{% endequation %}. אני חוזר על זה במפורש כל כך כי הצעד הבא של אוילר הוא לעבור לדבר על המכפלה <strong>האינסופית</strong> {% equation %}\prod_{t=1}^{\infty}\frac{1}{\left(1-x^{t}\right)}{% endequation %} ולטעון שהיא נותנת את הפונקציה היוצרת של חלוקות כלליות. אני מקווה שזה נשמע לנו אינטואיטיבי בשלב הזה, אבל מה בכלל המשמעות של מכפלה אינסופית שכזו? אי אפשר סתם לומר "כל האיברים שמתקבלים מפתיחת כל הסוגריים" כי דבר כזה יכלול "איברים" כמו {% equation %}x\cdot x^{2}\cdot x^{3}\cdots{% endequation %} שהחזקה שלהם יוצאת בעצמה סכום של מספרים טבעיים שאינו מתכנס (או שמתכנס ל-{% equation %}-\frac{1}{12}{% endequation %} <a href="http://gadial.net/2014/01/18/sum_of_naturals/">אם ממש בא לכם</a>, אבל זה לא מקדם אותנו). האינטואיציה שלנו היא שהאיברים היחידים ש"נחשבים" הם כאלו שכאשר פותחים את הסוגריים, מתקבלים רק ממספר <strong>סופי</strong> של מוכפלים שאינם 1. זה כמובן מה שקורה אצלנו.

אם זה לא פורמלי מספיק בשבילכם, הנה פסקה טכנית במיוחד שאני מקווה שתספיק לכם. צריך לקבל כאן מוסכמה כלשהי כדי לתת משהו לסימון הזה של מכפלה אינסופית - והמוסכמה היא שההגדרה של כפל תישאר בדיוק מה שהייתה במקרה הסופי. במקרה הסופי, הגדרנו {% equation %}\sum a_{n}\cdot\sum b_{n}=\sum c_{n}{% endequation %} כך ש-{% equation %}c_{n}=\sum_{k=0}^{n}a_{n}b_{n-k}{% endequation %}. אפשר לנסח את זה גם טיפה שונה: {% equation %}c_{n}=\sum_{k_{1}+k_{2}=n}a_{k_{1}}b_{k_{2}}{% endequation %}. כלומר, אנחנו עוברים על כל הפירוקים של {% equation %}n{% endequation %} לסכום שני טבעיים ומחברים את האיברים המתאימים ב-{% equation %}\sum a_{n}{% endequation %} ו-{% equation %}\sum b_{n}{% endequation %} עבורם. את זה קל להכליל לשלושה איברים: {% equation %}d_{n}=\sum_{k_{1}+k_{2}+k_{3}=n}a_{k_{1}}b_{k_{2}}c_{k_{3}}{% endequation %} וכן הלאה. עבור מכפלה אינסופית {% equation %}\prod_{k=1}^{\infty}\left(\sum a_{n}^{k}\right){% endequation %}, האיבר ה-{% equation %}n{% endequation %} יהיה שווה לסכום של כל האיברים מהצורה {% equation %}a_{t_{1}}^{k_{1}}\cdots a_{t_{r}}^{k_{r}}{% endequation %} כך ש-{% equation %}t_{1}+\dots+t_{r}=n{% endequation %} ואילו {% equation %}\left(k_{1},\dots,k_{r}\right){% endequation %} היא בחירה שרירותית כלשהי של {% equation %}r{% endequation %} טבעיים, כשהם מסודרים מהקטן לגדול. כל איבר בסכום הזה הוא בהכרח סופי כי הוא מכפלה סופית, אבל כדי שהעסק יהיה בעל משמעות צריך שיהיה רק מספר סופי של איברים בסכום הזה; כלומר, רק מספר סופי של בחירות {% equation %}\left(k_{1},\dots,k_{r}\right){% endequation %} שעבורן מתקבל {% equation %}a_{t_{1}}^{k_{1}}\cdots a_{t_{r}}^{k_{r}}\ne0{% endequation %}. אם זה לא המצב, אז המכפלה לא מוגדרת.

נסכם: המכפלה האינסופית סופרת, לכל {% equation %}n{% endequation %}, את מספר הפתרונות של המשוואה {% equation %}1\cdot x_{1}+2\cdot x_{2}+3\cdot x_{3}\dots=n{% endequation %}. פתרונות כאלו מראש מאלצים אותנו לתת 0 לכל המשתנים למעט מספר סופי; זה יתאים למכפלות שמתקבלות מפתיחת הסוגריים {% equation %}\left(1+x+x^{2}+\dots\right)\left(1+x^{2}+x^{4}+\dots\right){% endequation %} שבהן רק מספר סופי של מוכפלים הם של חזקות שונות מאפס, כלומר בוחרים "1" מכל הסוגריים למעט מספר סופי שלהן. זה מה שנותן לנו את המשוואה {% equation %}\sum_{n=0}^{\infty}p\left(n\right)x^{n}=\prod_{n=1}^{\infty}\frac{1}{\left(1-x^{n}\right)}{% endequation %}. כמובן שאם זה עדיין מרגיש "שגוי", כדאי לבצע את החישוב עצמאית, בעזרת ההגדרות שנתתי פה - זה יספיק.
<h2>פרק שלישי, שבו אולי יתברר למה השתלם לשרוד את כל הזוועות הטכניות הקודמות</h2>
עד עכשיו עניתי על השאלה מה זה בכלל פונקציות יוצרות ואיך אפשר למצוא אותן במקרה אחד ספציפי. כעת נשאלת השאלה - מה זה עוזר לנו? ובכן, זה עוזר להרבה דברים, אבל אני אראה רק אחד מהם: אם הפונקציות היוצרות הן פשוטות יחסית וניתנות להצגה בתור <strong>פונקציה רציונלית</strong>, אז אפשר לקבל מהן <strong>נוסחת נסיגה</strong> עבור הסדרה.

מה זו פונקציה רציונלית? מנה של שני פולינומים, כלומר משהו מהצורה {% equation %}\frac{s_{k}x^{k}+\dots+s_{1}x+s_{0}}{r_{t}x^{n}+\dots+r_{1}x+r_{0}}{% endequation %}. למשל, {% equation %}\frac{1}{1-x}{% endequation %} שראינו קודם היא פונקציה רציונלית. הנה עוד אחת: {% equation %}\frac{1}{1-x-x^{2}}{% endequation %}. מזהים את הסדרה שקשורה אליה? לא? אוקיי, אז בואו נסמן אותה בינתיים בתור {% equation %}a_{n}{% endequation %}, כרגיל; יש לנו את המשוואה {% equation %}\sum_{n=0}^{\infty}a_{n}x^{n}=\frac{1}{1-x-x^{2}}{% endequation %}. עכשיו, מה השוויון הזה אומר, פורמלית? שאם אכפול את אגף שמאל ב-{% equation %}1-x-x^{2}{% endequation %} אקבל 1. כלומר:

{% equation %}\left(\sum_{n=0}^{\infty}a_{n}x^{n}\right)\left(1-x-x^{2}\right)=1{% endequation %}

אם נפתח את הסוגריים ונקבץ איברים, נקבל את הסכום הבא:

{% equation %}1\cdot x^{0}+0\cdot x^{1}+0\cdot x^{2}+0\cdot x^{3}+\dots=\left(a_{0}\right)x^{0}+\left(a_{1}-a_{0}\right)x+\left(a_{2}-a_{1}-a_{0}\right)x^{2}+\left(a_{3}-a_{2}-a_{1}\right)x^{3}+\dots{% endequation %}

בדקו זאת! זה נובע ישירות מההגדרות שכבר ראינו. עכשיו, מה שבעצם קיבלנו הוא אינסוף משוואות, שמתקבלות מהשוואת המקדמים לכל חזקה של {% equation %}x{% endequation %}. כלומר, קיבלנו:
<ul>
 	<li>{% equation %}a_{0}=1{% endequation %}</li>
 	<li>{% equation %}a_{1}-a_{0}=0{% endequation %}</li>
 	<li>{% equation %}a_{2}-a_{1}-a_{0}=0{% endequation %}</li>
 	<li>{% equation %}a_{3}-a_{2}-a_{1}=0{% endequation %}</li>
</ul>
וכן הלאה. שתי המשוואות הראשונות נותנות לנו {% equation %}a_{0}=a_{1}=1{% endequation %} ואילו האחרות נותנות לנו {% equation %}a_{n}=a_{n-1}+a_{n-2}{% endequation %} באופן כללי. מזהים כעת? זו <strong>כמעט</strong> סדרת פיבונאצ'י: יש לה את נוסחת הנסיגה של פיבונאצ'י אבל תנאי התחלה ששוכחים את האיבר הראשון ה"אמיתי" שהוא {% equation %}0{% endequation %}. האם אפשר איכשהו לתקן את זה? בוודאי. בואו נסתכל על הפונקציה היוצרת {% equation %}\frac{x}{1-x-x^{2}}{% endequation %} שזהה לזו שראינו קודם פרט לכך שכפלנו את <strong>המונה</strong> ב-{% equation %}x{% endequation %}. כעת נקבל משוואות שמתחילות ב-
<ul>
 	<li>{% equation %}a_{0}=0{% endequation %}</li>
 	<li>{% equation %}a_{1}-a_{0}=1{% endequation %}</li>
 	<li>{% equation %}a_{2}-a_{1}-a_{0}=0{% endequation %}</li>
</ul>
וכן הלאה. ההבדל הוא בעצם רק באופן שבו שני האיברים הראשונים הוגדרו, וגם שם - רק במה שהיה באגף ימין.

בשתי הדוגמאות הללו בעצם מצויה כל התורה כולה: אם יש לנו פונקציה יוצרת רציונלית, המקדמים של <strong>המכנה</strong> מכתיבים לנו את <strong>נוסחת הנסיגה</strong> של הסדרה, בעוד שהמקדמים של <strong>המונה</strong> מכתיבים לנו את <strong>תנאי ההתחלה</strong> של הסדרה. אם המכנה הוא {% equation %}r_{t}x^{n}+\dots+r_{1}x+r_{0}{% endequation %} והמונה הוא {% equation %}s_{k}x^{k}+\dots+s_{1}x+s_{0}{% endequation %}, זה נותן לנו את הנוסחה הכללית

{% equation %}r_{0}a_{n}+r_{1}a_{n-1}+\dots+r_{t}a_{n-t}=s_{n}{% endequation %}

עבור {% equation %}n{% endequation %} גדול מספיק, {% equation %}s_{n}=0{% endequation %} תמיד, אז אנחנו מקבלים:

{% equation %}r_{0}a_{n}=-r_{1}a_{n-1}-\dots-r_{t}a_{n-t}{% endequation %}

זה מסביר את מה שקרה קודם - איך {% equation %}1-x-x^{2}{% endequation %} נתן לנו את נוסחת הנסיגה {% equation %}a_{n}=a_{n-1}+a_{n-2}{% endequation %} שאין בה מינוסים. הסימן של כל המקדמים למעט זה של החזקה הקטנה ביותר מתהפכים כשמבצעים את העברת האגף הזו.

עוד נקודה שכדאי לשים לב אליה היא שנוסחת הנסיגה הזו עובדת תמיד, לכל {% equation %}n{% endequation %}, גם כאלו קטנים. בואו נחזור לפיבונאצ'י: קודם כתבתי

{% equation %}a_{0}=1{% endequation %}

{% equation %}a_{1}-a_{0}=0{% endequation %}

אבל יכלתי באותה מידה בדיוק לכתוב

{% equation %}a_{0}-a_{-1}-a_{-2}=1{% endequation %}

{% equation %}a_{1}-a_{0}-a_{-1}=0{% endequation %}

תחת המוסכמה ש-{% equation %}a_{-1}=a_{-2}=0{% endequation %}. זה היה נותן מבנה אחיד לכל אגפי שמאל של המשוואות; ההבדל היחיד הוא באגף ימין, שמוכתב על ידי המונה של הפונקציה היוצרת.

אני מתעקש כל כך על דרך ההצגה הזו, כי עכשיו אני רוצה לעבור לדבר על המקרה שבו המונה והמכנה הם <strong>אינסופיים</strong>, כלומר אנחנו בסיטואציה הכללית שתיארתי קודם: {% equation %}\sum a_{n}x^{n}=\frac{\sum c_{n}x^{n}}{\sum b_{n}x^{n}}{% endequation %}. גם במקרה הזה הניתוח שעשינו קודם עובד - אני אקבל משוואות, פשוט קצת יותר מסובכות. הנה המשוואה הכללית:

{% equation %}b_{0}a_{n}+b_{1}a_{n-1}+\dots+b_{n}a_{0}+b_{n+1}a_{-1}+\dots=c_{n}{% endequation %}

מכיוון שההנחה היא ש-{% equation %}a_{-1}=a_{-2}=\dots=0{% endequation %}, אפשר למחוק את האיברים הללו מהסכום. אנחנו מקבלים משוואה עם מספר סופי של מחוברים

{% equation %}b_{0}a_{n}+b_{1}a_{n-1}+\dots+b_{n}a_{0}=c_{n}{% endequation %}

קשה לומר שהמשוואה הזו היא מה שאנחנו חושבים עליו בתור נוסחת נסיגה, בגלל שתי בעיות: ראשית, {% equation %}a_{n}{% endequation %} הופך כאן לתלוי <strong>בכל</strong> האיברים שבאים לפניו בסדרה ולא רק בשניים-שלושה קודמים. אבל זה עוד בסדר איכשהו. הבעיה העיקרית היא עם ה-{% equation %}c_{n}{% endequation %}-ים הללו באגף ימין, שקצת מוציאים את העוקץ מכל הסיפור אם הם לא פשוטים מספיק. הרי אם ה-{% equation %}c_{n}{% endequation %}-ים מסובכים, המרנו את הבעיה של לכתוב נוסחה מסודרת לערכים של {% equation %}a_{n}{% endequation %} בבעיה של לכתוב נוסחה מסודרת לערכים של {% equation %}c_{n}{% endequation %} ולא הרווחנו כלום. לכן פחות מעניין אותי המקרה של מונה אינסופי; אבל בהחלט אפשר לדבר על מה קורה כשהמונה סופי (בתקווה, 1) ואילו המכנה אינסופי. זה בדיוק המקרה של נוסחת הנסיגה שלנו עבור פונקציית החלוקה.
<h2>סיכום ביניים, ובו אני מתפייט על מה שעבורי כרגע היא הנוסחא היפה במתמטיקה</h2>
בואו נחזור אל שתי הנוסחאות שאיתן פתחנו:
<ul>
 	<li>{% equation %}\sum_{n=0}^{\infty}p\left(n\right)x^{n}=\prod_{n=1}^{\infty}\frac{1}{\left(1-x^{n}\right)}{% endequation %}</li>
 	<li>{% equation %}\prod_{n=1}^{\infty}\left(1-x^{n}\right)=\sum_{k=-\infty}^{\infty}\left(-1\right)^{k+1}x^{t\left(k\right)}{% endequation %} (כאשר {% equation %}t\left(k\right)=\frac{k\left(3k-1\right)}{2}{% endequation %})</li>
</ul>
הנוסחה השניה היא פשוט ההופכי של אגף ימין של הראשונה, כך שאם נשלב את שתי הנוסחאות ונכתוב את השניה במפורש, נקבל:

{% equation %}\sum_{n=0}^{\infty}p\left(n\right)x^{n}=\frac{1}{1-x-x^{2}+x^{5}+x^{7}-x^{12}-\dots}{% endequation %}

ועכשיו אני מקווה שכבר ברור למה זה נותן לנו את נוסחת הנסיגה שהצגתי בפתיחה:

{% equation %}p\left(n\right)=p\left(n-1\right)+p\left(n-2\right)-p\left(n-5\right)-p\left(n-7\right)+p\left(n-12\right)+\dots{% endequation %}

זה משאיר אותנו רק עם השאלה איך מוכיחים את הנוסחה השניה - זה לב העניין כאן והתוצאה היפה באמת לטעמי. אני אדבר על זה בפוסט הבא, אבל כבר עכשיו אפשר לקבל רעיון כללי לגבי מה בעצם הולך פה. כשפותחים את הביטוי {% equation %}\prod_{k=1}^{\infty}\left(1-x^{k}\right){% endequation %}, מה מקבלים? על פי שיקולים דומים לאלו שראינו קודם, הגורם {% equation %}x^{n}{% endequation %} מתקבל עבור כל חלוקה של {% equation %}n{% endequation %} למחוברים <strong>שונים</strong>, כשהסימן שלו הוא פלוס או מינוס בהתאם לזוגיות של מספר המחוברים. למשל, {% equation %}x^{3}{% endequation %} מתקבל מ-{% equation %}\left(1-x\right)\left(1-x^{2}\right)\left(1-x^{3}\right){% endequation %} בדיוק בשתי דרכים: הראשונה, כאשר אנחנו בוחרים משני הסוגריים הראשונים 1 ומהסוגריים האחרונים את {% equation %}-x^{3}{% endequation %}, ואז נקבל סימן שלילי; ואילו אם נבחר מהסוגריים הראשונים את {% equation %}-x{% endequation %} ומהשניים את {% equation %}-x^{2}{% endequation %} ומהאחרונים את {% equation %}1{% endequation %} נקבל {% equation %}\left(-x\right)\left(-x^{2}\right)=x^{3}{% endequation %} והפעם קיבלנו סימן חיובי. מכיוון ששני אלו בעלי סימנים מנוגדים, הם <strong>מבטלים זה את זה</strong> כאשר מחברים אותם, ואנחנו לא מקבלים את {% equation %}x^{3}{% endequation %} בכלל בסכום הסופי.

מה קורה עם {% equation %}x^{5}{% endequation %}? הנה הפירוקים שלו למספרים שונים: {% equation %}5,1+4,2+3{% endequation %}. כאן יש יתרון לפירוק למספר <strong>זוגי</strong> של מחוברים, ולכן הגורם {% equation %}x^{5}{% endequation %} יוצא חיובי בסכוםּ. לעומת זאת {% equation %}6{% endequation %} לא מופיע בסכום כי יש לו את הפירוקים {% equation %}6,1+5,2+4,1+2+3{% endequation %} - שניים זוגיים, שניים אי זוגיים, הכל מתבטל.

אם כן, את משפט המספרים המחומשים אפשר גם לנסח באופן הבא: לכל מספר טבעי {% equation %}n{% endequation %}, נסמן ב-{% equation %}p_{\text{odd}}\left(n\right){% endequation %} את מספר הפירוקים שלו לסכום מספרים <strong>שונים</strong> עם מספר <strong>אי זוגי</strong> של מחוברים, וב-{% equation %}p_{\text{even}}\left(n\right){% endequation %} את מספר הפירוקים לסכום מספרים <strong>שונים</strong> עם מספר <strong>זוגי</strong> של מחוברים. המשפט אומר שבדרך כלל {% equation %}p_{\text{odd}}\left(n\right)=p_{\text{even}}\left(n\right){% endequation %}, כשהיוצאים מן הכלל הם המספרים המחומשים, ובמקרה שלהם אחד משני המספרים יהיה גדול בדיוק ב-1 מהשני. במקרה שבו המספר המחומש הוא {% equation %}\frac{k\left(3k-1\right)}{2}{% endequation %} עם {% equation %}k{% endequation %} אי-זוגי אז מי שיהיה גדול יותר הוא {% equation %}p_{\text{odd}}\left(n\right){% endequation %}, ובמקרה השני זה יהיה {% equation %}p_{\text{even}}\left(n\right){% endequation %}.

הנוסחה {% equation %}\prod_{n=1}^{\infty}\left(1-x^{n}\right)=\sum_{k=-\infty}^{\infty}\left(-1\right)^{k+1}x^{\frac{k\left(3k-1\right)}{2}}{% endequation %} מקסימה לטעמי בגלל שהיא תופסת בצורה מאוד קומפקטית את המשפט הזה, על כל הסיבוך של הפירוק לסכום מחוברים, והספירה של כמה מחוברים יש וכן הלאה. אני לא חובב גדול של נוסחאות, אבל לטעמי הנוסחא הזו צריכה להופיע בכל רשימת "הנוסחאות היפות ביותר במתמטיקה" (מה שכמובן לא קורה). נו טוב.

בפוסט הבא: נוכיח את המשפט הזה סוף סוף! לפני זה קחו כמה דקות ונסו להוכיח את המשפט בעצמכם; אחרי שנתקלים שוב ושוב בקיר, כשרואים את הפתרון הוא גם ברור יותר וגם מלהיב הרבה יותר, כי ברור איך הוא עוקף את הקשיים.
