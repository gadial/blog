---
id: 2601
title: "פרוייקט \"התלמיד והמחשב\", בעיות 5-6-7"
date: 2013-07-01 08:00:41
layout: post
categories: 
  - תכנות
tags: 
  - פרוייקט "התלמיד והמחשב"
---
אנחנו ממשיכים לפתור בעיות טריוויאליות יחסית בפרוייקט "התלמיד והמחשב" - סבלנות ונגיע גם לדברים מעניינים יותר, אבל אני רוצה להיות נאמן לכל מה שהופיע בספר המקורי, גם אם אני הייתי כנראה כותב  אותו אחרת.

הפעם נעסוק בבעיות שמכריחות אותנו להציג מרכיב חשוב חדש של כל שפת תכנות - <strong>משפטי תנאי!</strong> הרעיון במשפטי תנאי הוא לגרום לתוכנית להתפצל בין שתי (או יותר) אפשרויות שונות, וזאת בניגוד לכל מה שעשינו עד כה שבו התוכנית פשוט הריצה את כל הפקודות שהיו כתובות בתוכנית.

<strong>בעיה מס' 5</strong>

בבעיה הזו מקבלים כקלט שני מספרים שלמים וצריך להגיד אם הם שווי סימן או שוני סימן. כלומר, האם אחד מהם חיובי והשני שלילי. הבדיקה המתמטית הקצרה שאפשר לבצע כאן היא האם המכפלה של המספרים היא חיובית או שלילית; אם היא חיובית הם שווי סימן ואם היא שלילית הם שוני סימן. ומה אם היא אפס? אפשר לקבוע שרירותית שאז הם שווי סימן כדי לחסוך לנו כאב ראש.

ברובי זה קל מאוד:

[code language="ruby"]
x, y = ARGV[0].to_i, ARGV[1].to_i
puts &quot;#{x} and #{y} have equal signs&quot; if x*y &gt;= 0
puts &quot;#{x} and #{y} have different signs&quot; if x*y &lt; 0
[/code]

אני חושב שהקוד קריא אפילו למי שבכלל לא מכיר את התחביר של רובי, אבל בכל זאת כדאי להתעמק טיפה במה שקורה פה. אנחנו מתחילים עם שורה של קליטת קלט רגילה, ואחריה מגיעה פקודת puts רגילה, אבל באותה שורה, אחרי פקודת ה-puts פתאום מופיע if, שמשמעותו - את מה שהיה כתוב בשורה הזו בצע רק אם תנאי מסויים מתקיים. ומה התנאי הזה? שהמכפלה של x,y היא גדולה או שווה ל-0.

מה שאני משתמש בו בשורה הזו הוא סוג חדש של <strong>אופרטור</strong>. אופרטור הוא משהו שלוקח ערכים קיימים ומפיק מהם ערך חדש ולרוב יש לו סימון מיוחד בתוך שפת התכנות עצמה, למשל כפל שמסומן בכוכבית. הסימן של "גדול שווה" הוא סוג אחר של אופרטור - אופרטור בוליאני. כזה שלוקח שני ערכים שאפשר להשוות ביניהם, ומחזיר כפלט ערך שהוא או True או False - "נכון" או "לא נכון", או אם תרצו - "אמת" או "שקר".
פקודת if מקבלת כקלט ערך בוליאני כזה. אם הוא True, אז פקודת ה-if מתבצעת (דהיינו, במקרה שלנו, השורה שהפקודה מגיעה בסופה תתבצע). אם היא קיבלה False, הפקודה לא מתבצעת. זה הכל, לבינתיים. בהמשך נראה סוגים מורכבים יותר של אופרטורים בוליאניים.

הערה חשובה אחת היא שסגנון הכתיבה הזה של רובי הוא לא סטנדרטי בשפות תכנות אחרות. ברובן ה-if מגיע <strong>לפני</strong> הפקודה שמתבצעת. גם ברובי אפשר לכתוב את זה ככה, ועוד נראה זאת בהמשך, אבל כשרוצים להתנות ביצוע של שורה אחת בלבד אפשר לשים את ה-if גם בסוף של השורה כפי שעשיתי כאן. אני אישית אוהב את סגנון הכתיבה הזה וחושב שהוא משפר את קריאות הקוד; אני בהחלט יכול להבין גם אנשים ששונאים אותו ובטוחים שזה הדבר הגרוע ביותר מאז המצאת ה-goto. אם אתם לא אוהבים את סגנון הכתיבה הזה - אל תשתמשו בו. זה לא הכרח.

בואו נעבור לראות איך עושים משפטי תנאי בגישה שונה לחלוטין - הגישה ההסקלית:

[code]
sign_equality :: Int -&gt; (Int -&gt; String)
sign_equality a b
	| 0 &lt;= a*b 	= &quot;equal&quot;
	| 0 &gt; a*b	= &quot;different&quot;

main = do
  putStrLn &quot;Please insert two numbers to compare their signs&quot;
  a &lt;- getLine
  b &lt;- getLine
  putStrLn (a ++ &quot; and &quot; ++ b ++ &quot; have &quot; ++ (sign_equality (read a) (read b)) ++ &quot; signs&quot;)
[/code]

מה שאני עושה פה הוא להגדיר פונקציה שמקבלת שני מספרים ומחזירה את המחרוזת "equal" אם הסימנים שלהם שווים, ואת המחרוזת "different" אם הם שונים. הפונקציה הזו מוגדרת באופן כמו-מתמטי, באמצעות חלוקה למקרים, כשכל מקרה מתחיל בסימן | של קו עומד. כל קו עומד כזה נקרא Guard - "שומר". הרעיון בשומרים הוא פשוט: כדי לדעת איזה ערך הפונקציה תחזיר, היא עוברת שומר שומר. כל שומר מורכב מסימן הקו העומד, ואחריו תנאי, ולבסוף = וערך כלשהו. הפונקציה בודקת את התנאים באופן סדרתי עד שהיא מגיעה אל התנאי הראשון שמתקיים, ואז מחזירה את הערך שאחרי סימן ה-= שלו.

אתם עשויים לתהות מה קורה אם אף אחד מהתנאים שאחרי השומרים לא מתקיים - מה הפונקציה תחזיר אז? ובכן, אין חוכמות - הפונקציה תיכשל והתוכנית תקרוס אם השגיאה הזו לא תטופל. לכן לרוב רצוי מאוד שהשומרים יטפלו בכל המקרים האפשריים; כדי לעשות את החיים פשוטים, נהוג להשתמש במילת המפתח otherwise עבור השומר האחרון (בפועל otherwise הוא פשוט שם אחר ל-True, מה שמבטיח שהתנאי הזה תמיד יתקיים) ולתת לו את ערך "ברירת המחדל" של הפונקציה; זה שאמור להיות מוחזר ממנה אם כל הבדיקות האחרות נכשלו. עוד נראה את זה בהמשך, אני מקווה.

וכעת לג'אווהסקריפט, שבה אני אנצל את ההזדמנות כדי להציג גישה <strong>נוספת</strong> לתנאים:

[code language="javascript"]
&lt;html&gt;
&lt;head&gt;
&lt;title&gt;Targil 5&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
  &lt;script type=&quot;text/javascript&quot;&gt;
    compute_sign_relation = function(){
		var a = parseInt(document.getElementById(&quot;a&quot;).value);
		var b = parseInt(document.getElementById(&quot;b&quot;).value);
		var sign_relation = (a*b &gt;= 0)?(&quot;equal&quot;):(&quot;different&quot;);
		document.getElementById(&quot;sign_relation&quot;).innerHTML = &quot;Signs are &quot; + sign_relation;
    }
  &lt;/script&gt;
  a = &lt;input type=&quot;textbox&quot; id=&quot;a&quot; value = &quot;0&quot; onkeyup = &quot;compute_sign_relation()&quot;/&gt;
  &lt;br /&gt;
  b = &lt;input type=&quot;textbox&quot; id=&quot;b&quot; value = &quot;0&quot; onkeyup = &quot;compute_sign_relation()&quot;/&gt;
  &lt;br /&gt;
  &lt;div type=&quot;label&quot; id=&quot;sign_relation&quot;/&gt;&lt;/div&gt;
&lt;/body&gt;
&lt;/html&gt;
[/code]

אין ממש צורך לקרוא את הכל - שורת המפתח המעניינת פה היא זו:

<p dir="ltr">
sign_relation = (a*b >= 0)?("equal"):("different")
</p>

מה הולך פה? יש כאן שימוש ב<strong>אופרטור הטרנרי</strong> ("טרנרי" פירושו "על שלושה ערכים"). זה אופרטור שמקבל שלושה קלטים, כאשר בין הראשון לשני מפריד סימן שאלה ובין השני לשלישי מפרידות נקודותיים. הקלט הראשון אמור להיות ערך בוליאני, אבל שני האחרים יכולים להיות מה שתרצו. כך שהפעלה של האופרטור באופן כללי נראית כך:

<p dir="ltr">
CONDITION ? VAR_TRUE : VAR_FALSE
</p>

אם התנאי CONDITION הוא True, אז האופרטור יחזיר את הערך של VAR_TRUE. אם התנאי הוא False, אז האופרטור יחזיר את VAR_FALSE.

למה לעשות את זה כך? למה לא להשתמש במשפט תנאי? ובכן, ההבדל המהותי הוא שמשפט תנאי הוא Statement, כלומר פקודה שצריכה לעמוד בשורה משל עצמה; לעומת זאת, האופרטור הטרנרי הוא Expression - ניתן לשלב אותו כחלק משורות פקודה גדולות יותר. בהמשך נראה (בתקווה) סיטואציות שבהן משמעותית יותר נוח להשתמש בו מאשר במשפט תנאי בשורה נפרדת (אבל שלא יהיה ספק - מדובר על עניין של נוחות נטו ולא משהו מעבר לכך).

כדאי להעיר כי כמובן, האופרטור הטרנרי אינו המצאה של ג'אווהסקריפט ויש אותו בשלל שפות נוספות, ובפרט ברובי (דווקא בפייתון - שנחשבת לשפה ידידותית מאוד - לא היה אותו במשך פרק זמן ארוך, וכיום יש אותו אבל עם תחביר שונה מזה שהצגתי כאן).

<strong>בעיות מס' 6 ו-7</strong>

בבעיה מס' 6 הקלט הוא צלעות של משולש, ויש להוציא לפלט הודעה האם הוא שווה צלעות או לא. בבעיה מס' 7 הקלט הוא צלעות משולש ויש להוציא לפלט הודעה האם הוא שווה שוקיים או לא. אלו שתי בעיות דומות מאוד מבחינה רעיונית ולכן אני פותר את שתיהן יחד; יהיה יותר מאתגר לכתוב קוד שצריך לטפל בו זמנית בשלושת המקרים האפשריים: או שווה צלעות, או שווה שוקיים, או כלום.

הפתרון שלי ברובי יהיה שמרני משהו מבחינת הסגנון שלו, כדי להראות את הצורה ה"רגילה" שבה כותבים תנאים בשפות תכנות. בפרט אני הולך להכניס לתמונה את else שמטפל במה שקורה אם משפט תנאי <strong>לא</strong> מתקיים:

[code language="ruby"]
a, b, c = ARGV

if (a == b and b == c)
  puts &quot;Equilateral triangle&quot;
elsif (a == b or b == c or a == c)
  puts &quot;Isosceles triangle&quot;
else
  puts &quot;Not equilateral and not isosceles triangle&quot;
end
[/code]

שימו לב לקליטת הפרמטרים בהתחלה - אני אפילו לא טורח להמיר אותם למספרים, כי הערכים המספריים לא חשובים - רק אם הם שווים או שונים, ואת זה אפשר לבדוק גם עבור מחרוזות. כמו כן, צורת הכתיבה נראית קצת מוזרה - בצד שמאל יש לי שלושה משתנים ובצד ימין יש לי רק משתנה אחד - אבל המשתנה הזה, ARGV, הוא מערך - רשימה של ערכים - וכשאני כותב שלושה משתנים מופרדים בפסיקים בצד ימין ומבצע השמה זו דרך מקוצרת לומר "קח את שלושת הערכים הראשונים מתוך ARGV והצב אותם ב-a,b,c".

שאר התוכנית היא המחשה לשימוש סטנדרטי ב-if. המבנה הכללי של if בנוי כך: ראשית כתוב if ואז תנאי בוליאני; אחר כך יורדים שורה ומתחילים לכתוב פקודות שאמורות להתבצע אם ה-if התקיים, ובסופו של אוסף הפקודות הזה כותבים end אם רוצים פשוט לסיים. אבל לא תמיד רוצים לסיים - לפעמים רוצים להגיד "אם ה-if לא התבצע, אז בצע כך וכך". לשם כך משתמשים ב-else. אלא שלפעמים רוצים להגיד "אם ה-if לא התבצע, בדוק תנאי חדש ואם הוא מתבצע, אז...". ברובי משתמשים ב-elsif כדי לתאר את זה.

קרוב לודאי שאתם תוהים למה לא לכתוב else if כמו בני אדם; הסיבה לכך היא טכנית ודי מעיקה: אם נכתוב else ואז if, אז ה-if יפתח לנו בלוק פקודות חדש, ואז נצטרך לסיים אותו ב-end ואחר כך יבוא ה-end של בלוק הפקודות הראשון של ה-if הראשון. זה מסורבל ומבלבל ועשוי לגרום לבאגים מכאן ועד להודעה חדשה ולכן לא נוקטים בגישה הזו.

עכשיו אפשר להסתכל על התוכן של הקוד הספציפי הזה. מבחינה רעיונית נכון יותר לבדוק קודם אם המשולש שווה צלעות; אם הוא שווה צלעות ברור שהוא שווה שוקיים, אבל ממילא נרצה לומר שהוא שווה צלעות ולא שווה שוקיים. לכן הבדיקה הראשונה היא אם המשולש שווה צלעות. לשם כך מספיק לבדוק אם a שווה ל-b ואם b שווה ל-c, כי אם שני הזוגות הללו שווים, גם a יהיה שווה ל-c (זוהי תכונת <strong>הטרנזיטיביות</strong> של השוויון). יש לנו כאן שני תנאים לבדוק, ולכן מחברים ביניהם עם and, שהוא בעצמו אופרטור בוליאני שמקבל שני ערכים בוליאנים ומחזיר True אם שניהם True ואחרת מחזיר False. בשפות כמו C משתמשים ב-&& במקום ב-and עבור האופרטור הזה; ברובי מעדיפים את הכתיב היותר "מילולי", ואני מעדיף זאת בעצמי.

אם התנאי הראשון לא התקיים, בודקים את התנאי הנדרש לכך שהמשולש יהיה שווה שוקיים, כלומר שיהיו שתי צלעות שוות. כאן יש לנו שלוש בדיקות לבצע, שמחוברות עם האופרטור "או" (or) שמחזיר True אם אחד משני הערכים שהוא מקבל הוא True (אגב, "ערך שאופרטור מקבל" נקרא "<strong>אופרנד</strong>"). אם התנאי הזה הצליח מוציאים הודעה מתאימה; אחרת אנחנו יודעים שהמשולש אינו שווה צלעות וגם אינו שווה שוקיים ואנחנו מוציאים הודעה מתאימה ומסיימים.

נעבור לגישה ההסקלית:

[code]
triangle_type :: Int -&gt; (Int -&gt; (Int -&gt; String))
triangle_type a b c
	| a == b &amp;&amp; b == c				= &quot;Equilateral&quot;
	| a == b || b == c || a == c	= &quot;Isosceles&quot;
	| otherwise						= &quot;Not equilateral and not isosceles&quot;


main = do
  putStrLn &quot;Please insert two numbers to compare their signs&quot;
  a &lt;- getLine
  b &lt;- getLine
  c &lt;- getLine
  putStrLn ((triangle_type (read a) (read b) (read c)) ++ &quot; triangle&quot;)
[/code]

כאן אפשר לראות שימוש ב-&& בתור האופרטור and וב-|| בתור האופרטור or, במיטב המסורת של C. כמו כן, אפשר לראות איך צורת הכתיבה ההסקלית מטפלת בתנאים בצורה יותר נקיה: אין צורך ב-else וב-elsif למיניהם, אלא פשוט בתנאים שהולכים על הראשון מביניהם שמתקיים וחסל.

הקוד בג'אווהסקריפט הוא הסטנדרטי מכולם:

[code language="javascript"]
&lt;html&gt;
&lt;head&gt;
&lt;title&gt;Targil 6-7&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
  &lt;script type=&quot;text/javascript&quot;&gt;
    check_triangle_type = function(){
		var a = parseInt(document.getElementById(&quot;a&quot;).value);
		var b = parseInt(document.getElementById(&quot;b&quot;).value);
		var c = parseInt(document.getElementById(&quot;c&quot;).value);
		var triangle_type;
		if (a == b &amp;&amp; b == c){
		  triangle_type = &quot;Equilateral triangle&quot;;
		}
		else if (a == b || b == c || a == c){
		  triangle_type = &quot;Isosceles triangle&quot;;
		}
		else {
		  triangle_type = &quot;Not equilateral and not isosceles triangle&quot;;
		}
		document.getElementById(&quot;triangle_type&quot;).innerHTML = triangle_type;
    }
  &lt;/script&gt;
  a = &lt;input type=&quot;textbox&quot; id=&quot;a&quot; value = &quot;0&quot; onkeyup = &quot;check_triangle_type()&quot;/&gt;
  &lt;br /&gt;
  b = &lt;input type=&quot;textbox&quot; id=&quot;b&quot; value = &quot;0&quot; onkeyup = &quot;check_triangle_type()&quot;/&gt;
  &lt;br /&gt;
  c = &lt;input type=&quot;textbox&quot; id=&quot;c&quot; value = &quot;0&quot; onkeyup = &quot;check_triangle_type()&quot;/&gt;
  &lt;br /&gt;
  &lt;div type=&quot;label&quot; id=&quot;triangle_type&quot;/&gt;Equilateral triangle&lt;/div&gt;
&lt;/body&gt;
&lt;/html&gt;
[/code]

מבחינה מהותית זה אותו הקוד כמו זה של רובי, רק עם התחביר השונה של ג'אווהסקריפט שמזכיר יותר את התחביר של C, עם סוגריים מסולסלים לכל בלוק, ועם else if במקום elsif (כאן else if הוא בדיוק זה - פקודת else שאחריה בלוק בן פקודה אחת - ובלוק כזה לא צריך סוגריים מסולסלים סביבו - כשאותה פקודה היא בעצמה פקודת if שבאה עם בלוק משל עצמה). חשוב לציין שאני משתמש כאן במוסכמת קוד אפשרית אחת - הסוגר המסולסל השמאלי של בלוק if בא מייד לאחר הסוגריים של התנאי (אגב, הסוגריים הללו הם רשות ברובי אבל ברוב השפות הן חובה). אפשר היה גם לשים אותם בשורה נפרדת משל עצמם. מיותר לציין שהמריבות בשאלה אם נכון לשים את הסוגר המסולסל בסוף הסוגריים של ה-if או שהוא צריך להיות בשורה משל עצמו מגמדות את המלחמות של ליליפוט ובלפוסקו.